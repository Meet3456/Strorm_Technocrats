


import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
from flask_cors import CORS
import random
import difflib
import pickle
from urllib.parse import urlparse
import socket
import ssl
import whois
import requests
import time
import datetime
import dns.resolver
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
import asyncio
from pyppeteer import launch
from skimage import io, measure
import os
import subprocess
from skimage.metrics import structural_similarity as ssim
import aiohttp
from aiofiles import open as aio_open
from selenium import webdriver
import pyautogui
from PIL import Image

app = Flask(__name__)
CORS(app)

model = keras.models.load_model('models/final_model.h5')
def calculate_ssim(image_path1, image_path2):
    # Open the images using PIL
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)

    # Convert images to grayscale
    image1 = image1.convert("L")
    image2 = image2.convert("L")
    
    # Ensure both images have the same dimensions
    if image1.size != image2.size:
        # Resize the larger image to match the dimensions of the smaller image
        width1, height1 = image1.size
        width2, height2 = image2.size
        if width1 * height1 > width2 * height2:
            image1 = image1.resize((width2, height2), Image.ANTIALIAS)
        else:
            image2 = image2.resize((width1, height1), Image.ANTIALIAS)
    
    # Convert images to numpy arrays
    image1 = np.array(image1)
    image2 = np.array(image2)
    
    # Calculate SSIM score
    score = ssim(image1, image2)
    return score


async def capture_screenshot(url, output_path):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    await page.screenshot({'path': output_path})
    await browser.close()

# def create_event_loop():
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)

# async def capture_screenshot(url, output_path):
#     browser = await launch()
#     page = await browser.newPage()
#     await page.goto(url)
#     await page.screenshot({'path': output_path})
#     await browser.close()

# def calculate_ssim(url1, url2):
#     output_dir = "Backend/screenshots"
#     os.makedirs(output_dir, exist_ok=True)
    
#     output_path1 = os.path.join(output_dir, "s1.png")
#     output_path2 = os.path.join(output_dir, "s2.png")

#     asyncio.run(capture_screenshot(url1, output_path1))
#     asyncio.run(capture_screenshot(url2, output_path2))

#     image1 = io.imread(output_path1)
#     image2 = io.imread(output_path2)
    
#     ssim_score = measure.compare_ssim(image1, image2, multichannel=True)

#     return round(ssim_score, 2)


def url_parser(url):
    # Parse the URL to extract its components
    parsed_url = urlparse(url)

    # Features related to the entire URL
    qty_dot_url = url.count('.')
    qty_hyphen_url = url.count('-')
    qty_underline_url = url.count('_')
    qty_slash_url = url.count('/')
    qty_questionmark_url = url.count('?')
    qty_equal_url = url.count('=')
    qty_at_url = url.count('@')
    qty_and_url = url.count('&')
    qty_exclamation_url = url.count('!')
    qty_space_url = url.count(' ')
    qty_tilde_url = url.count('~')
    qty_comma_url = url.count(',')
    qty_plus_url = url.count('+')
    qty_asterisk_url = url.count('*')
    qty_hashtag_url = url.count('#')
    qty_dollar_url = url.count('$')
    qty_percent_url = url.count('%')
    length_tld_url = len(parsed_url.netloc.split('.')[-1])
    length_url = len(url)
    print("sab barabar checkpoint")
    # Features related to the domain
    domain = parsed_url.netloc
    qty_dot_domain = domain.count('.')
    qty_hyphen_domain = domain.count('-')
    qty_underline_domain = domain.count('_')
    qty_slash_domain = domain.count('/')
    qty_questionmark_domain = domain.count('?')
    qty_equal_domain = domain.count('=')
    qty_at_domain = domain.count('@')
    qty_and_domain = domain.count('&')
    qty_exclamation_domain = domain.count('!')
    qty_space_domain = domain.count(' ')
    qty_tilde_domain = domain.count('~')
    qty_comma_domain = domain.count(',')
    qty_plus_domain = domain.count('+')
    qty_asterisk_domain = domain.count('*')
    qty_hashtag_domain = domain.count('#')
    qty_dollar_domain = domain.count('$')
    qty_percent_domain = domain.count('%')
    qty_vowels_domain = sum(1 for char in domain if char.lower() in 'aeiouAEIOU')
    domain_length = len(domain)
    domain_in_ip = 0
    server_client_domain = 'server' in domain.lower() or 'client' in domain.lower()

    # Features related to the path (directory and file)
    path = parsed_url.path
    qty_dot_directory = path.count('.')
    qty_hyphen_directory = path.count('-')
    qty_underline_directory = path.count('_')
    qty_slash_directory = path.count('/')
    qty_questionmark_directory = path.count('?')
    qty_equal_directory = path.count('=')
    qty_at_directory = path.count('@')
    qty_and_directory = path.count('&')
    qty_exclamation_directory = path.count('!')
    qty_space_directory = path.count(' ')
    qty_tilde_directory = path.count('~')
    qty_comma_directory = path.count(',')
    qty_plus_directory = path.count('+')
    qty_asterisk_directory = path.count('*')
    qty_hashtag_directory = path.count('#')
    qty_dollar_directory = path.count('$')
    qty_percent_directory = path.count('%')
    directory_length = len(path)

    # Features related to the file (last part of the path)
    file = path.split('/')[-1]
    qty_dot_file = file.count('.')
    qty_hyphen_file = file.count('-')
    qty_underline_file = file.count('_')
    qty_slash_file = file.count('/')
    qty_questionmark_file = file.count('?')
    qty_equal_file = file.count('=')
    qty_at_file = file.count('@')
    qty_and_file = file.count('&')
    qty_exclamation_file = file.count('!')
    qty_space_file = file.count(' ')
    qty_tilde_file = file.count('~')
    qty_comma_file = file.count(',')
    qty_plus_file = file.count('+')
    qty_asterisk_file = file.count('*')
    qty_hashtag_file = file.count('#')
    qty_dollar_file = file.count('$')
    qty_percent_file = file.count('%')
    file_length = len(file)

    # Features related to query parameters
    params = parsed_url.query
    qty_dot_params = params.count('.')
    qty_hyphen_params = params.count('-')
    qty_underline_params = params.count('_')
    qty_slash_params = params.count('/')
    qty_questionmark_params = params.count('?')
    qty_equal_params = params.count('=')
    qty_at_params = params.count('@')
    qty_and_params = params.count('&')
    qty_exclamation_params = params.count('!')
    qty_space_params = params.count(' ')
    qty_tilde_params = params.count('~')
    qty_comma_params = params.count(',')
    qty_plus_params = params.count('+')
    qty_asterisk_params = params.count('*')
    qty_hashtag_params = params.count('#')
    qty_dollar_params = params.count('$')
    qty_percent_params = params.count('%')
    params_length = len(params)
    
    # Features related to query parameters
    tld_present_params = parsed_url.netloc.split('.')[-1] in parsed_url.query
    qty_params = len(parsed_url.query.split('&'))

    # Features related to email presence in URL
    email_in_url = '@' in url
    
    # Features related to domain lookup time
    try:
        # domain_ip = socket.gethostbyname(parsed_url.netloc)
        start_time = time.time()
        response = requests.get(url)
        lookup_time = time.time() - start_time
    except (socket.gaierror, requests.exceptions.RequestException):
        lookup_time = 0
        
    
    # Features related to SPF (Sender Policy Framework)
    spf_record = 0
    try:
        spf_record = dns.resolver.resolve(parsed_url.netloc, 'TXT')
        # domain_spf = any(record.to_text().startswith('v=spf1') for record in spf_record)
        domain_spf = 1
    except:
        domain_spf = 0 

    # Features related to ASN (Autonomous System Number)
    try:
        ip_info = 1
        asn_ip = 1
    except socket.gaierror:
        asn_ip = 0

    # Features related to domain WHOIS information
    try:
        domain_info = whois.whois(parsed_url.netloc)
        time_domain_activation = (domain_info.creation_date - datetime.datetime.now()).days
        time_domain_expiration = (domain_info.expiration_date - datetime.datetime.now()).days
    except (AttributeError, TypeError):
        time_domain_activation = 0
        time_domain_expiration = 0

        # Features related to resolved IPs, name servers, and MX servers
    try:
        ips = socket.gethostbyname_ex(parsed_url.netloc)
        qty_ip_resolved = len(ips[2])
        qty_nameservers = len(socket.gethostbyname_ex(parsed_url.netloc)[0])
        mx_record = dns.resolver.resolve(parsed_url.netloc, 'MX')
        qty_mx_servers = len(mx_record)
    except (socket.gaierror, dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
        qty_ip_resolved = 0
        qty_nameservers = 0
        qty_mx_servers = 0

    # Features related to TTL (Time-to-Live)
    try:
        ttl_hostname = socket.gethostbyname(parsed_url.netloc)
        ttl_hostname = socket.gethostbyaddr(ttl_hostname)[1]
        ttl_hostname = 1
    except (socket.gaierror, socket.herror):
        ttl_hostname = 0

    # Features related to TLS/SSL certificate
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=parsed_url.netloc) as s:
            s.connect((parsed_url.netloc, 443))
            tls_ssl_certificate = s.getpeercert() is not None
    except (socket.gaierror, ConnectionRefusedError, ssl.CertificateError):
        tls_ssl_certificate = 0

    # Features related to redirects
    try:
        response = requests.head(url, allow_redirects=True)
        qty_redirects = len(response.history)
    except requests.exceptions.RequestException:
        qty_redirects = 0

    # Features related to Google indexing
    def is_url_indexed_on_google(url):
        google_search_url = f"https://www.google.com/search?q=site:{url}"
        try:
            response = requests.get(google_search_url)
            return "did not match any documents" not in response.text
        except requests.exceptions.RequestException:
            return 0

    url_google_index = is_url_indexed_on_google(parsed_url.netloc)
    domain_google_index = is_url_indexed_on_google(f"www.{parsed_url.netloc}")
    if domain_google_index == True:
        domain_google_index = 1
    else:
        domain_google_index = 0
    if url_google_index == True:
        url_google_index = 1
    else:
        url_google_index = 0

    # Features related to URL shortening
    # url_shortened = len(url) < 20
    if len(url) < 20:
        url_shortened = 1
    else:
        url_shortened = 0

    # Return the extracted features as a dictionary
    features = {
        "qty_dot_url": qty_dot_url,
        "qty_hyphen_url": qty_hyphen_url,
        "qty_underline_url": qty_underline_url,
        "qty_slash_url": qty_slash_url,
        "qty_questionmark_url": qty_questionmark_url,
        "qty_equal_url": qty_equal_url,
        "qty_at_url": qty_at_url,
        "qty_and_url": qty_and_url,
        "qty_exclamation_url": qty_exclamation_url,
        "qty_space_url": qty_space_url,
        "qty_tilde_url": qty_tilde_url,
        "qty_comma_url": qty_comma_url,
        "qty_plus_url": qty_plus_url,
        "qty_asterisk_url": qty_asterisk_url,
        "qty_hashtag_url": qty_hashtag_url,
        "qty_dollar_url": qty_dollar_url,
        "qty_percent_url": qty_percent_url,
        "length_tld_url": length_tld_url,
        "length_url": length_url,
        "qty_dot_domain": qty_dot_domain,
        "qty_hyphen_domain": qty_hyphen_domain,
        "qty_underline_domain": qty_underline_domain,
        "qty_slash_domain": qty_slash_domain,
        "qty_questionmark_domain": qty_questionmark_domain,
        "qty_equal_domain": qty_equal_domain,
        "qty_at_domain": qty_at_domain,
        "qty_and_domain": qty_and_domain,
        "qty_exclamation_domain": qty_exclamation_domain,
        "qty_space_domain": qty_space_domain,
        "qty_tilde_domain": qty_tilde_domain,
        "qty_comma_domain": qty_comma_domain,
        "qty_plus_domain": qty_plus_domain,
        "qty_asterisk_domain": qty_asterisk_domain,
        "qty_hashtag_domain": qty_hashtag_domain,
        "qty_dollar_domain": qty_dollar_domain,
        "qty_percent_domain": qty_percent_domain,
        "qty_vowels_domain": qty_vowels_domain,
        "domain_length": domain_length,
        "domain_in_ip": domain_in_ip,
        "server_client_domain": server_client_domain,
        "qty_dot_directory": qty_dot_directory,
        "qty_hyphen_directory": qty_hyphen_directory,
        "qty_underline_directory": qty_underline_directory,
        "qty_slash_directory": qty_slash_directory,
        "qty_questionmark_directory": qty_questionmark_directory,
        "qty_equal_directory": qty_equal_directory,
        "qty_at_directory": qty_at_directory,
        "qty_and_directory": qty_and_directory,
        "qty_exclamation_directory": qty_exclamation_directory,
        "qty_space_directory": qty_space_directory,
        "qty_tilde_directory": qty_tilde_directory,
        "qty_comma_directory": qty_comma_directory,
        "qty_plus_directory": qty_plus_directory,
        "qty_asterisk_directory": qty_asterisk_directory,
        "qty_hashtag_directory": qty_hashtag_directory,
        "qty_dollar_directory": qty_dollar_directory,
        "qty_percent_directory": qty_percent_directory,
        "directory_length": directory_length,
        "qty_dot_file": qty_dot_file,
        "qty_hyphen_file": qty_hyphen_file,
        "qty_underline_file": qty_underline_file,
        "qty_slash_file": qty_slash_file,
        "qty_questionmark_file": qty_questionmark_file,
        "qty_equal_file": qty_equal_file,
        "qty_at_file": qty_at_file,
        "qty_and_file": qty_and_file,
        "qty_exclamation_file": qty_exclamation_file,
        "qty_space_file": qty_space_file,
        "qty_tilde_file": qty_tilde_file,
        "qty_comma_file": qty_comma_file,
        "qty_plus_file": qty_plus_file,
        "qty_asterisk_file": qty_asterisk_file,
        "qty_hashtag_file": qty_hashtag_file,
        "qty_dollar_file": qty_dollar_file,
        "qty_percent_file": qty_percent_file,
        "file_length": file_length,
        "qty_dot_params": qty_dot_params,
        "qty_hyphen_params": qty_hyphen_params,
        "qty_underline_params": qty_underline_params,
        "qty_slash_params": qty_slash_params,
        "qty_questionmark_params": qty_questionmark_params,
        "qty_equal_params": qty_equal_params,
        "qty_at_params": qty_at_params,
        "qty_and_params": qty_and_params,
        "qty_exclamation_params": qty_exclamation_params,
        "qty_space_params": qty_space_params,
        "qty_tilde_params": qty_tilde_params,
        "qty_comma_params": qty_comma_params,
        "qty_plus_params": qty_plus_params,
        "qty_asterisk_params": qty_asterisk_params,
        "qty_hashtag_params": qty_hashtag_params,
        "qty_dollar_params": qty_dollar_params,
        "qty_percent_params": qty_percent_params,
        "params_length": params_length,
        "tld_present_params": tld_present_params,
        "qty_params": qty_params,
        "email_in_url": email_in_url,
        "time_response": lookup_time,
        "domain_spf": domain_spf,
        "asn_ip": asn_ip,
        "time_domain_activation": time_domain_activation,
        "time_domain_expiration": time_domain_expiration,
        "qty_ip_resolved": qty_ip_resolved,
        "qty_nameservers": qty_nameservers,
        "qty_mx_servers": qty_mx_servers,
        "ttl_hostname": ttl_hostname,
        "tls_ssl_certificate": tls_ssl_certificate,
        "qty_redirects": qty_redirects,
        "url_google_index": url_google_index,
        "domain_google_index": domain_google_index,
        "url_shortened": url_shortened,
    }

    return features

@app.route("/")
def home():
    print("Congrats server chal rha hai!!!")
    return "<h1>Hello</h1>"

@app.route("/url", methods=['POST'])
def predict():
    print("Atleast ye function run ho rha hai")
    request_data = request.get_json()
    url = request_data.get("url")
    print(url)
    try:
        print("Idhar aaya but aage jana")
        print(url)
        # Extract features from the URL
        features = url_parser(url)

        print("features aagaya yay!!!")
        # scaler = MinMaxScaler()
        # Convert features to a format suitable for prediction
        # feature_values = np.array(list(features.values())).reshape(1, -1)
        # feature_values = feature_values.reshape(1, -1)
        # print(len(feature_values))
        # input_data = np.array([feature_values])
        # input_data = feature_values
        # input_shape = model.input_shape
        # print("Expected input shape:", input_shape)
        # input_data = scaler.fit_transform(feature_values)
        # print(input_data.shape)
        # Use your machine learning model to make predictions
        feature_values = list(features.values())

        # Check the length of the feature_values list
        print(feature_values)  # This should print 111

        # Convert the feature_values list into a NumPy array with shape (1, 111)
        input_data = np.array([feature_values])
        print("iske aage hagga")
        prediction = model.predict(input_data)
        print(prediction)
        # Return the prediction as JSON response
        prediction_value = prediction[0]

        # Check if the prediction value is greater than 0.5
        if prediction_value > 0.75:
            response = {"prediction": "Legitimate"}
        else:
            response = {"prediction": "Phishing site"}

        # Return the prediction as JSON response
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route("/compare", methods=["POST"])
def compare():
    try:
        request_data = request.get_json()
        url = request_data.get("url")

        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()

        output_dir = "Backend/screenshots"
        screenshot_path = os.path.join(output_dir, "ss.png")

        pyautogui.screenshot(screenshot_path)
        driver.quit()

        companies = ['google', 'Microsoft', 'Apple', 'Amazon', 'Flipkart', 'Netflix',  'Prime', 'Facebook', 'Insta', 'Axis', 'BankofAmerica']
        from urllib.parse import urlparse
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        set1 = set(domain)
        fruits = []

        for i in companies:
            set2 = set(i)
            intersection = len(set1.intersection(set2))
            union = len(set1.union(set2))
            fruits.append(intersection / union)

        max_index = fruits.index(max(fruits))
        image_folder = companies[max_index]
        image_files = os.listdir("Backend/Data/" + image_folder)

        max_ssim_score = -1
        matching_image = None

        for image_file in image_files:
            image_path = os.path.join("Backend/Data/", companies[max_index], image_file)
            ss = Image.open(screenshot_path)
            og = Image.open(image_path)

            width1, height1 = ss.size
            width2, height2 = og.size

            if (width1, height1) != (width2, height2):
                if width1 * height1 > width2 * height2:
                    ss = ss.resize((width2, height2))
                else:
                    og = og.resize((width1, height1))

            # Convert the PIL images to file paths and then calculate SSIM
            ss_path = os.path.join(output_dir, "ss_temp.png")
            og_path = os.path.join(output_dir, "og_temp.png")
            ss_path_react = os.path.join("Frontend/src/Component", "ss_temp.png")
            og_path_react = os.path.join("Frontend/src/Component", "og_temp.png")

            ss.save(ss_path)
            ss.save(ss_path_react)
            og.save(og_path_react)
            og.save(og_path)

            ssim_score = calculate_ssim(ss_path, og_path)

            if ssim_score > max_ssim_score:
                max_ssim_score = ssim_score
                matching_image = image_file

        if matching_image:
            response = {"max_ssim_score": round(max_ssim_score, 2)}
        else:
            response = {"message": "No matching image found."}

        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)})



if __name__ == "__main__":
    app.run(debug = True)