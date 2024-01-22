Currency Converter ₹ to $

server side code:- 

# flask_currency_converter.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_currency():
   try:
      data = request.json
      amount_in_rs = data['amount_in_rs']
      conversion_rate = 0.012  # Replace with the actual conversion rate

      amount_in_usd = amount_in_rs * conversion_rate
      return jsonify({'amount_in_usd': format(amount_in_usd, '.4f')})

   except Exception as e:
      return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
   app.run(debug=True)


client side code:- 

// Java code to call the service

import java.net.HttpURLConnection;
import java.net.URL;
import java.io.OutputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class JavaClient {
   public static void main(String[] args) throws Exception {
      String url = "http://localhost:5000/convert";

      // JSON payload
      System.out.print("Enter the amount you want to convert: ");
      Scanner scanner = new Scanner(System.in);

      double amountInRs = scanner.nextDouble();
      String jsonInputString = "{\"amount_in_rs\": "+amountInRs+"}";
      scanner.close();

      URL obj = new URL(url);
      HttpURLConnection con = (HttpURLConnection) obj.openConnection();
      con.setRequestMethod("POST");
      con.setRequestProperty("Content-Type", "application/json");

      // Send POST request
      con.setDoOutput(true);
      OutputStream os = con.getOutputStream();
      os.write(jsonInputString.getBytes());
      os.flush();
      os.close();

      // Get response
      int responseCode = con.getResponseCode();
      BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
      String inputLine;
      StringBuffer response = new StringBuffer();

      while ((inputLine = in.readLine()) != null) {
         response.append(inputLine);
      }
      in.close();

      // Print result
      System.out.println("Response Code: " + responseCode);
      System.out.println("Response: " + response.toString());
   }
}

