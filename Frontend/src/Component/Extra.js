import React, { useState } from "react";
import Navbar from "./Navbar";
import design from "../assets/design.svg";
import image from "../assets/phishing-image.webp";
import danger from "../assets/danger.png";
import safe from "../assets/safe.png";
import ImageDisplay from "./ImageDisplay";
import axios from "axios";
import ss from "./ss_temp.png";
import og from "./og_temp.png";

const Extra = () => {
  const [url, setUrl] = useState("");
  const [ssImageUrl, setssImageUrl] = useState("");
  const [ogImageUrl, setOgImageUrl] = useState("");
  const [similarityScore, setSimilarityScore] = useState(null);
  const [isValidUrl, setIsValidUrl] = useState(true);
  const [isPhish, setIsPhish] = useState(null);

  const handleUrlChange = async (e) => {
    let enteredUrl = e.target.value.trim();

    console.log("Entered URL:", enteredUrl);
    // Check if the user has entered a domain without a protocol
    if (
      enteredUrl.length > 0 &&
      !enteredUrl.startsWith("http://") &&
      !enteredUrl.startsWith("https://")
    ) {
      // Automatically append 'https://' to the domain
      enteredUrl = "https://" + enteredUrl;
    }

    setUrl(enteredUrl);
    setIsValidUrl(true);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    let enteredUrl = url;
    console.log("Entered URL:", enteredUrl);
    try {
      const response = await fetch("/url", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ url: enteredUrl }),
      });
      console.log();
      if (!response.ok) {
        throw new Error("Failed to send the URL to Server");
      }

      let result = await response.json();
      setIsPhish(result);

      // console.log(result.prediction);
    } catch (error) {
      console.error("Error", error.message);
    }
    // Regular expression for a more comprehensive URL validation
    const urlRegex = /^(ftp|http|https):\/\/[^ "]+$/;

    if (urlRegex.test(url)) {
      // URL is valid, you can proceed with your logic here
      console.log("Valid URL:", url);
    } else {
      // URL is not valid
      setIsValidUrl(false);
    }
  };

  const handle = async () => {
    try {
      const response = await axios.post("http://localhost:5000/compare", {
        url,
      });
      const max_ssim_score = response.data;

      console.log("max_ssim_score ", max_ssim_score);

      // setSsImageUrl(`/path/to/screenshot-image`); // Replace with your screenshot image path
      // setOgImageUrl(`/path/to/${matching_image}`); // Replace with your matched image path
      setSimilarityScore(max_ssim_score);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };
  return (
    <div className='bg text-white'>
      <Navbar />
      <div>
        <div className='items-center flex justify-center mt-[200px] '>
          <div>
            <label
              htmlFor='website'
              className='block mb-2 text-2xl font-medium text-gray-900 dark:text-white'
            >
              Website URL
            </label>
            <div
              className={`bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 space-x-2 ${
                !isValidUrl && "border-red-500"
              }`}
            >
              <input
                type='url'
                id='website'
                className='w-[400px] h-[50px] rounded'
                placeholder=' https://example.com'
                value={url}
                onChange={handleUrlChange}
                required
              />
              <button
                className='bg-rose-600 w-[140px] h-[40px] hover:bg-white hover:text-rose-800 text-white font-bold rounded'
                onClick={handleSubmit}
              >
                Submit
              </button>
            </div>
            {!isValidUrl && (
              <p className='text-red-500 text-sm mt-2'>
                Please enter a valid URL.
              </p>
            )}
          </div>
        </div>
        <div className='flex space-x-5 justify-center items-center'>
          <h1 className='text-center mt-5 text-[2rem] font-bold'>
            {isPhish?.prediction}
          </h1>
          <img
            src={isPhish?.prediction === "Legitimate" ? safe : danger}
            alt={isPhish?.prediction === "Legitimate" ? "Safe Image" : "Danger"}
            className={`w-${
              isPhish?.prediction === "Legitimate" ? "10" : "16"
            } h-${isPhish?.prediction === "Legitimate" ? "10" : "16"} mt-${
              isPhish?.prediction === "Legitimate" ? "0" : "3"
            }`}
            style={{
              display: isPhish?.prediction === "Legitimate" ? "block" : "none",
            }}
          />
        </div>

        <img src={design} alt='design' />
      </div>

      {/* -------------------------------------------------------------------------------------------------------------------------- */}
      <div className='w-full h-screen'>
        <div>
          <h1 className='text-[2.5rem] ml-[38%] mt-[2%] regular'>
            Phishing Image Comparison
          </h1>
          <div className='items-center'>
            {/* <label>Enter URL:</label>
              <input
                type='url'
                id='website'
                className='w-[400px] h-[50px] rounded'
                placeholder=' https://example.com'
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                required
              /> */}
            <div>
              <label
                htmlFor='website'
                className='block mb-2 text-2xl font-medium text-gray-900 dark:text-white'
              >
                Website URL
              </label>
              <div className={`${!isValidUrl && "border-red-500"}`}>
                <input
                  type='url'
                  id='website'
                  className='w-[400px] h-[50px] rounded'
                  placeholder=' https://example.com'
                  value={url}
                  onChange={(e) => setUrl(e.target.value)}
                  required
                />
                <button
                  className='absolute bg-rose-600 ml-[1rem] w-[140px] h-[40px] text-white font-bold rounded'
                  onClick={handle}
                >
                  Compare
                </button>
              </div>
            </div>
            {/* <input
              type='text'
              value={url}
              onChange={(e) => setUrl(e.target.value)}
            /> */}
          </div>

          {similarityScore !== null && (
            <div>
              <div className='flex space-x-3'>
                <div className='p-5'>
                  <p className='text-[2rem] items-center'>
                    Screenshot by Sellium
                  </p>
                  <img src={ss} style={{ maxWidth: "100%" }} />
                </div>
                <div className='p-5'>
                  <p className='text-[2rem]'>Original / Exisiting Website</p>
                  <img src={og} style={{ maxWidth: "100%" }} />
                </div>
              </div>
              <p className='text-[2.5rem] ml-[38%]'>
                Similarity Score: {similarityScore.max_ssim_score}
              </p>
              {/* <ImageDisplay imageUrl='./ss_temp.png' altText='Screenshot' /> */}
              {/* <ImageDisplay imageUrl='og_temp.png' altText='Matched Image' /> */}
            </div>
          )}
        </div>
      </div>
      {/* 
   ------------------------------------------------------------------------- */}
      {/* <div className=''>
        <div className='w-full h-[5rem] bg-rose-900 regular '>
          <h1 className='text-white text-[3.5rem] ml-[36%]'>
            What is Phishing ?
          </h1>
        </div>
        <div className='flex items-center space-x-20 mt-10'>
          <img src={image} alt='phishing' className='ml-20' />
          <h1 className='text-[1.5rem] p-12'>
            Phishing is a type of cybersecurity attack during which malicious
            actors send messages pretending to be a trusted person or entity.
            Phishing messages manipulate a user, causing them to perform actions
            like installing a malicious file, clicking a malicious link, or
            divulging sensitive information such as access credentials. Phishing
            is the most common type of social engineering, which is a general
            term describing attempts to manipulate or trick computer users.
            Social engineering is an increasingly common threat vector used in
            almost all security incidents. Social engineering attacks, like
            phishing, are often combined with other threats, such as malware,
            code injection, and network attacks.
          </h1>
        </div>
      </div>       */}
    </div>
  );
};

export default Extra;
