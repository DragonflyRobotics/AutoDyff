import com.google.common.io.CharStreams;
import org.json.JSONObject;

import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;
import java.io.BufferedReader;
import javax.net.ssl.HttpsURLConnection;

public class serverRequestTest {
    public static void main(String[] args) {

        final String serverEndpoint = "https://www.codermerlin.academy/vapor/brennan-coil/numerical_engine/endpoint";
        final String[] result = new String[1];
        /*
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter a valid formula to take the derivative of: ");
        String expression = scan.nextLine();
        System.out.println("Please enter the x value: ");
        String x_value = scan.nextLine();
        System.out.println("Please wait, processing formula...");

        try {
            JSONObject userJsonObject = new JSONObject();
            userJsonObject.put("equation", expression);
            userJsonObject.put("x", x_value);

            URL serverEndpointURL = new URL(serverEndpoint);
            HttpsURLConnection httpConnection = (HttpsURLConnection) serverEndpointURL.openConnection();
            httpConnection.setRequestMethod("POST");
            httpConnection.setRequestProperty("Content-Type", "application/json");
            httpConnection.setRequestProperty("Accept", "text/plain");
            httpConnection.setDoInput(true);
            httpConnection.setDoOutput(true);
            httpConnection.getOutputStream().write(userJsonObject.toString().getBytes(StandardCharsets.UTF_8));
            httpConnection.getOutputStream().close();

            BufferedReader reader = new BufferedReader(new InputStreamReader(httpConnection.getInputStream()));
            StringBuilder response = new StringBuilder();

            while (reader.readLine() != null) {
                System.out.println(reader.readLine());
                response.append(reader.readLine());
            }

            result[0] = response.toString();
            System.out.println(result.length);

            System.out.println("The result is: " + result[0]);
        } catch (Exception e) {
            result[0] = "Error: " + e.getMessage();
            System.out.println(result[0]);
        } */
        try {
            // Create the command
            ProcessBuilder processBuilder = new ProcessBuilder(
                    "curl",
                    "--header", "Content-Type: application/json",
                    "--request", "POST",
                    "--data", "{\"equation\": \"x^2\", \"x\": \"5\"}",
                    "https://codermerlin.academy/vapor/brennan-coil/numerical_engine/endpoint"
            );

            // Redirect error stream to output stream
            processBuilder.redirectErrorStream(true);

            // Start the process
            Process process = processBuilder.start();

            // Read the output of the process
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            StringBuilder response = new StringBuilder();

            while (reader.readLine() != null) {
                response.append(reader.readLine());
            }

            // Wait for the process to complete
            //int exitCode = process.waitFor();
            //System.out.println("Process exited with code " + exitCode);
            System.out.println(response);
        } catch (Exception e) {
            System.out.println("You suck");
        }
    }
}

