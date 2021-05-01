import React, { useState } from "react";
import axios from "axios";
import { VscRunAll } from "react-icons/vsc";
import Loader from "react-loader-spinner";

export default function Warnings({ code }) {
  const [warnings, setWarnings] = useState("Click on Show Warnings Button");
  const [isLoading, setLoading] = useState(false);

  const onSubmitCode = async (e) => {
    try {
      e.preventDefault();
      setLoading(true);

      const res = await axios.post(
        "https://pseudo-x.herokuapp.com/api/v1/warnings/",
        {
          source: code,
          test: "",
        }
      );

      setLoading(false);

      var war;

      for (var i = 0; i < res.data.length; i++) {
        war += res.data[i] + "\n";
      }

      console.log(war);

      setWarnings(war);

      // console.log(res.data.run_status);
    } catch (err) {
      setLoading(false);
      console.log(err);
    }
  };

  return (
    <div className="p-8 pt-5">
      <div role="alert">
        <div class="bg-red-500 text-white flex justify-between font-bold rounded-t px-4 py-2">
          <div>Code Suggestions</div>
          <div className="px-2 pl-3 bg-gray-600 hover:bg-gray-400 rounded-md">
            <button
              onClick={onSubmitCode}
              className="pt-1 mb-1 m-0 outline-none focus:outline-none"
            >
              <VscRunAll size="22" />
            </button>
          </div>
        </div>
        <div class="border border-t-0  rounded-b h-auto bg-red-100 px-4 py-3 text-red-800">
          {isLoading ? (
            <Loader
              className="pl-72"
              type="Rings"
              color="#00BFFF"
              height={80}
              width={80}
            />
          ) : (
            <div className="whitespace-pre-wrap">{warnings}</div>
          )}
        </div>
      </div>
    </div>
  );
}
