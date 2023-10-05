import React from 'react'
import Navbar from './Navbar'
import one from '../assets/one.svg'
import two from '../assets/two.svg'
import Footer from './Footer'

const About = () => {
    return (
        <div className='overflow-x-hidden'>
            <section class="text-gray-600 body-font w-screen mt-[800px]">
                <div class="container mx-auto flex px-5 py-24 md:flex-row flex-col items-center">
                    <div class="lg:max-w-lg lg:w-full md:w-1/2 w-5/6 mb-10 md:mb-0">
                        <img class="object-cover object-center rounded" alt="hero" src={one} />
                    </div>
                    <div class="lg:flex-grow md:w-1/2 lg:pl-24 md:pl-16 flex flex-col md:items-start md:text-left items-center text-center">
                        <h1 class="title-font sm:text-4xl text-5xl mb-4 font-bold text-gray-900">Start phishing in minutes
                        </h1>
                        <p class="mb-8 leading-relaxed text-[1.3rem]">Zero installations and simple configuration makes setting usecure up an absolute breeze. Once you're in, simply upload your users via integration or CSV, then you're ready to start phishing!</p>
                        <div class="flex justify-center">

                            <ul class="max-w-md space-y-1 text-black list-inside text-black text-[1rem]">
                                <li class="flex items-center text-black text-[1.3rem]">
                                    <svg class="w-3.5 h-3.5 mr-2 text-green-500 dark:text-green-400 flex-shrink-0" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                                        <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z" />
                                    </svg>
                                    Automated Phishing Domain Identification
                                </li>
                                <li class="flex items-center text-[1.3rem]">
                                    <svg class="w-3.5 h-3.5 mr-2 text-green-500 dark:text-green-400 flex-shrink-0" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                                        <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z" />
                                    </svg>
                                    Multi-Faceted Analysis Using WHOIS Data
                                </li>
                                <li class="flex items-center text-[1.3rem]">
                                    <svg class="w-3.5 h-3.5 mr-2 text-green-500 dark:text-green-400 flex-shrink-0" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                                        <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z" />
                                    </svg>
                                    Image-Based Phishing Detection with Probability Scores
                                </li>
                            </ul>

                        </div>
                    </div>
                </div>
            </section>


            <section class="text-gray-600 body-font">
                <div class="container mx-auto flex px-5 py-24 md:flex-row flex-col items-center">
                    <div class="lg:flex-grow md:w-1/2 lg:pl-24 md:pl-16 flex flex-col md:items-start md:text-left items-center text-center">
                        <h1 class="title-font sm:text-4xl text-5xl mb-4 font-bold text-gray-900">Monitor ongoing vulnerability
                        </h1>
                        <p class="mb-8 leading-relaxed text-[1.3rem]">With new staff, changing work environments and ever-evolving phishing threats, assessing ongoing risk is crucial. With the AutoPhish feature, you can enable regular simulations that measure user resilience over time.</p>
                        <div class="flex justify-center">

                            <ul class="max-w-md space-y-1 text-black list-inside text-black text-[1rem]">
                                <li class="flex items-center text-black text-[1.3rem]">
                                    <svg class="w-3.5 h-3.5 mr-2 text-green-500 dark:text-green-400 flex-shrink-0" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                                        <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z" />
                                    </svg>
                                    Automate simulations (AutoPhish)
                                </li>
                                <li class="flex items-center text-[1.3rem]">
                                    <svg class="w-3.5 h-3.5 mr-2 text-green-500 dark:text-green-400 flex-shrink-0" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                                        <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z" />
                                    </svg>
                                    Test different phishing techniques
                                </li>
                                <li class="flex items-center text-[1.3rem]">
                                    <svg class="w-3.5 h-3.5 mr-2 text-green-500 dark:text-green-400 flex-shrink-0" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                                        <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z" />
                                    </svg>
                                    Get weekly summary reports
                                </li>
                            </ul>

                        </div>
                    </div>
                    <div class="lg:max-w-lg lg:w-full md:w-1/2 w-5/6 mb-10 md:mb-0">
                        <img class="object-cover object-center rounded" alt="hero" src={two} />
                    </div>

                </div>
            </section>
            <Footer/>
        </div>
    )
}

export default About