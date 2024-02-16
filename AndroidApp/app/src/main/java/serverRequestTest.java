import org.json.JSONObject;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;
import java.io.BufferedReader;

public class serverRequestTest {
    public static void main(String[] args) {

        final String serverEndpoint = "https://www.codermerlin.academy/vapor/brennan-coil/numerical_engine/endpoint";
        String result;

        Scanner scan = new Scanner(System.in);
        System.out.println("Enter a valid formula to take the derivative of: ");
        String expression = scan.nextLine();
        System.out.println("Please enter the x value: ");
        String x_value = scan.nextLine();

        try {
            JSONObject userJsonObject = new JSONObject();
            userJsonObject.put("equation", expression);
            userJsonObject.put("x", x_value);

            URL serverEndpointURL = new URL(serverEndpoint);
            HttpURLConnection httpConnection = (HttpURLConnection) serverEndpointURL.openConnection();
            httpConnection.setRequestMethod("POST");
            httpConnection.setRequestProperty("Content-Type", "application/json");
            //httpConnection.setRequestProperty("Accept", "text/plain");
            httpConnection.setDoInput(true);
            httpConnection.setDoOutput(true);
            httpConnection.getOutputStream().write(userJsonObject.toString().getBytes(StandardCharsets.UTF_8));
            httpConnection.getOutputStream().close();

            BufferedReader reader = new BufferedReader(new InputStreamReader(httpConnection.getInputStream()));

            /* Only one line of response outputted; no need to do a while loop
            Furthermore, this loop is incorrectly implemented as it can potentially
            skip past non-null values and pass in null values accidentally
            (data loss potential).
            while (reader.readLine() != null) {
                response.append(reader.readLine());
            }
            */

            result = reader.readLine();
            System.out.println("The result is: " + result);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }


        /* CURL request unneeded

        try {
            // Create the command
            ProcessBuilder processBuilder = new ProcessBuilder(
                    "curl",
                    "--header", "Content-Type: application/json",
                    "--request", "POST",
                    "--data", "{\"equation\": \"x^2\", \"x\": \"5\"}",
                    serverEndpoint
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

        */


    }
}

