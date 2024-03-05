package com.example.betterapp;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;

import android.annotation.SuppressLint;

import android.os.Bundle;
import android.util.DisplayMetrics;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;

import java.net.URL;
import java.net.HttpURLConnection;
import java.nio.charset.StandardCharsets;

import io.reactivex.rxjava3.android.schedulers.AndroidSchedulers;
import io.reactivex.rxjava3.annotations.NonNull;
import io.reactivex.rxjava3.core.Observable;
import io.reactivex.rxjava3.core.ObservableSource;
import io.reactivex.rxjava3.core.Observer;
import io.reactivex.rxjava3.disposables.CompositeDisposable;
import io.reactivex.rxjava3.functions.Supplier;
import io.reactivex.rxjava3.observers.DisposableObserver;
import io.reactivex.rxjava3.schedulers.Schedulers;

public class MainActivity extends AppCompatActivity
    implements View.OnClickListener {
    private static final String TAG = "MainActivity";

    private final CompositeDisposable disposables = new CompositeDisposable();

    TextView resultText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        DisplayMetrics displayMetrics = new DisplayMetrics();
        getWindowManager().getDefaultDisplay().getMetrics(displayMetrics);
        float displayHeight = displayMetrics.heightPixels;
        int displayWidth = displayMetrics.widthPixels;

        TextView titleText = findViewById(R.id.titleText);
        titleText.setTextSize(displayHeight * 0.02f);

        TextView equationLabelText = findViewById(R.id.equationInputLabel);
        equationLabelText.setTextSize((int) (displayHeight * 0.01));
        equationLabelText.setHeight((int) (displayHeight * 0.05));
        ConstraintLayout.LayoutParams labelTextParams = (ConstraintLayout.LayoutParams) equationLabelText.getLayoutParams();
        labelTextParams.topMargin = (int) (displayHeight * 0.03);
        equationLabelText.setLayoutParams(labelTextParams);


        EditText equationInputField = findViewById(R.id.userEquationInputField);
        equationInputField.setWidth(displayWidth/2);
        equationInputField.setHeight((int) (displayHeight * 0.05));
        ConstraintLayout.LayoutParams textFieldParams = (ConstraintLayout.LayoutParams) equationInputField.getLayoutParams();
        textFieldParams.setMarginStart((int) (displayWidth * 0.02));
        textFieldParams.topMargin = (int) (displayHeight * 0.03);
        equationInputField.setLayoutParams(textFieldParams);

        TextView x_valueLabelText = findViewById(R.id.user_x_valueInputLabel);
        x_valueLabelText.setTextSize((int) (displayHeight * 0.01));
        x_valueLabelText.setHeight((int) (displayHeight * 0.05));
        ConstraintLayout.LayoutParams x_valueLabelParams = (ConstraintLayout.LayoutParams) x_valueLabelText.getLayoutParams();
        x_valueLabelParams.topMargin = (int) (displayHeight * 0.03);
        x_valueLabelText.setLayoutParams(x_valueLabelParams);

        EditText x_valueInputField = findViewById(R.id.user_x_valueInputField);
        x_valueInputField.setWidth(displayWidth/2);
        x_valueInputField.setHeight((int) (displayHeight * 0.05));
        ConstraintLayout.LayoutParams x_valueInputParams = (ConstraintLayout.LayoutParams) x_valueInputField.getLayoutParams();
        x_valueInputParams.setMarginStart((int) (displayWidth * 0.02));
        x_valueInputParams.topMargin = (int) (displayHeight * 0.03);
        x_valueInputField.setLayoutParams(x_valueInputParams);

        Button inputConfirmButton = findViewById(R.id.inputConfirmButton);
        inputConfirmButton.setWidth(displayWidth/3);
        inputConfirmButton.setHeight((int) (displayHeight/15));
        inputConfirmButton.setTextSize(displayHeight * 0.01f);
        ConstraintLayout.LayoutParams inputConfirmButtonParams = (ConstraintLayout.LayoutParams) inputConfirmButton.getLayoutParams();
        inputConfirmButtonParams.topMargin = (int) (displayHeight * 0.03);
        inputConfirmButton.setLayoutParams(inputConfirmButtonParams);
        inputConfirmButton.setOnClickListener(this);

        // Set the result title
        TextView resultHeader = findViewById(R.id.resultHeader);
        resultHeader.setTextSize(displayHeight * 0.01f);
        ConstraintLayout.LayoutParams resultHeaderParams = (ConstraintLayout.LayoutParams) resultHeader.getLayoutParams();
        resultHeaderParams.topMargin = (int) (displayHeight * 0.05f);
        resultHeader.setLayoutParams(resultHeaderParams);

        this.resultText = findViewById(R.id.resultText);
        resultText.setTextSize(displayHeight * 0.008f);
        resultText.setHeight((int) (displayHeight * 0.3));

        Button faxButton = findViewById(R.id.faxButton);
	faxButton.setTextSize(displayHeight * 0.01f);
        faxButton.setOnClickListener(this);
    }


    /*   Test user input processing
    public String possibleInput(String input) {
        switch (input.toLowerCase()) {
            case "krishna":
                return "Absolute AI maniac!";
            case "brennan":
                return "Breeno the Cheerio head (Ed Sheeran?!)";
            case "aryan":
                return "Get back to work!!! enthusiast";
            case "nikson":
                return "Goofy goober";
            default:
                return "additional functionalities yet to be added...";
        }
    }

         */


    @SuppressLint({"NonConstantResourceId", "SetTextI18n"})
    @Override
    public void onClick(View v) {
        if (v.getId() == R.id.faxButton) {
            Toast.makeText(this, R.string.toast_text, Toast.LENGTH_SHORT).show();
        } else if (v.getId() == R.id.inputConfirmButton) {
            EditText equation = findViewById(R.id.userEquationInputField);
            EditText x_value = findViewById(R.id.user_x_valueInputField);
            disposables.add(
                    apiRequestObservable(equation.getText().toString(), x_value.getText().toString())
                            .subscribeOn(Schedulers.io())
                            .observeOn(AndroidSchedulers.mainThread())
                            .subscribe(result -> resultText.setText(result))
            );
        }
    }

    static Observable<String> apiRequestObservable(String equation, String x_value) {
        return Observable.defer(new Supplier<ObservableSource<? extends String>>() {
            @Override public ObservableSource<? extends String> get() throws Throwable {
                // Do some long running operation
                String response = apiRequest(equation, x_value);
                return Observable.just(response);
            }
        });
    }

    public static String apiRequest(String equation, String x_value) {
        final String serverEndpoint = "https://www.codermerlin.academy/vapor/brennan-coil/numerical_engine/endpoint";

        try {
            JSONObject userJsonObject = new JSONObject();
            userJsonObject.put("equation", equation);
            userJsonObject.put("x", x_value);

            URL serverEndpointURL = new URL(serverEndpoint);
            HttpURLConnection httpConnection = (HttpURLConnection) serverEndpointURL.openConnection();
            httpConnection.setRequestMethod("POST");
            httpConnection.setRequestProperty("Content-Type", "application/json");
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

            return reader.readLine();
        } catch (Exception e) {
            return "Error: " + e.getMessage();
        }
    }
    
    
    @Override
    protected void onDestroy() {
        super.onDestroy();
        disposables.clear();
    }
}
