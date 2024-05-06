package com.example.betterapp.ui.home;

import androidx.annotation.DisplayContext;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModelProvider;

import android.content.ContextParams;
import android.graphics.Rect;
import android.net.Uri;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import android.util.DisplayMetrics;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.WindowManager;
import android.view.WindowMetrics;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.VideoView;

import com.example.betterapp.R;

import org.json.JSONObject;
import org.w3c.dom.Text;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;

import io.reactivex.rxjava3.android.schedulers.AndroidSchedulers;
import io.reactivex.rxjava3.core.Observable;
import io.reactivex.rxjava3.core.ObservableSource;
import io.reactivex.rxjava3.disposables.CompositeDisposable;
import io.reactivex.rxjava3.functions.Supplier;
import io.reactivex.rxjava3.schedulers.Schedulers;

public class HomeFragment extends Fragment {

    private HomeViewModel mViewModel;
    private static final String TAG = "HomeFragment";
    private final CompositeDisposable disposables = new CompositeDisposable();
    MutableLiveData<String> resultLiveData = new MutableLiveData<>();

    public static HomeFragment newInstance() {
        return new HomeFragment();
    }

    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container,
                             @Nullable Bundle savedInstanceState) {

        WindowManager windowManager = requireActivity().getWindowManager();
        View rootView = inflater.inflate(R.layout.fragment_home, container, false);

        // these methods are deprecated
        //DisplayMetrics displayMetrics = new DisplayMetrics();
        //windowManager.getDefaultDisplay().getMetrics(displayMetrics);

        // get android device dimensions
        Rect screenRect = windowManager.getCurrentWindowMetrics().getBounds();

        float displayHeight = screenRect.height();
        int displayWidth = screenRect.width();

        // deprecated due to use of banner.svg as banner/title on the activity_main.xml instead
        // set title text display
        //TextView titleText = rootView.findViewById(R.id.titleText);
        //titleText.setTextSize(displayHeight * 0.015f);

        // set equation input label display size and its location
        TextView equationLabelText = rootView.findViewById(R.id.equationInputLabel);
        setEquationLabel(displayHeight, equationLabelText);

        //set equation input field display size and its location
        EditText equationInputField = rootView.findViewById(R.id.userEquationInputField);
        setEquationField(displayHeight, displayWidth, equationInputField);

        // set x_value input label display size and its location
        TextView x_valueLabelText = rootView.findViewById(R.id.user_x_valueInputLabel);
        setX_valueLabel(displayHeight, x_valueLabelText);

        // set x_value input field display size and its location
        EditText x_valueInputField = rootView.findViewById(R.id.user_x_valueInputField);
        setX_valueInputField(displayHeight, displayWidth, x_valueInputField);

        // Set the result header
        TextView resultHeader = rootView.findViewById(R.id.resultHeader);
        setResultHeader(displayHeight,resultHeader);

        // set result display size and location
        TextView resultText = rootView.findViewById(R.id.resultText);
        setResultText(displayHeight,resultText);


        // set confirmation button display size and its location
        Button inputConfirmButton = rootView.findViewById(R.id.inputConfirmButton);
        setInputConfirmButton(displayHeight, displayWidth, inputConfirmButton);
        inputConfirmButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                EditText equation = rootView.findViewById(R.id.userEquationInputField);
                EditText x_value = rootView.findViewById(R.id.user_x_valueInputField);
                // make an asynchronous request on Schedulers.io for server request
                // and then subscribe on the main android thread to display the result within the result text view
                disposables.add(
                        apiRequestObservable(equation.getText().toString(), x_value.getText().toString())
                                .subscribeOn(Schedulers.io())
                                .observeOn(AndroidSchedulers.mainThread())
                                .subscribe(result -> {
                                    resultLiveData.setValue(result);
                                    resultText.setText(resultLiveData.getValue());
                                })
                );
            }
        });

        //return inflater.inflate(R.layout.fragment_home, container, false);
        return rootView;
    }

    /* Deprecated due to impracticality
       'Programmatic event handling' is far more cohesive and concise
       than using 'XML-defined event handling'
    @SuppressLint({"NonConstantResourceId", "SetTextI18n"})
    @Override
    public void onClick(View v) {
        if (v.getId() == R.id.inputConfirmButton) {
            EditText equation = rootView.findViewById(R.id.userEquationInputField);
            EditText x_value = rootView.findViewById(R.id.user_x_valueInputField);
            // make an asynchronous request on Schedulers.io for server request
            // and then subscribe on the main android thread to display the result within the result text view
           disposables.add(
                    apiRequestObservable(equation.getText().toString(), x_value.getText().toString())
                            .subscribeOn(Schedulers.io())
                            .observeOn(AndroidSchedulers.mainThread())
                            .subscribe(result -> {
                                resultLiveData.setValue(result);
                                resultText.setText(resultLiveData.getValue());
                            })
            );
        }
    }
     */

    public static void setBanner() {

    }
    public static void setEquationLabel(float displayHeight, TextView equationLabel) {
        equationLabel.setTextSize((int) (displayHeight * 0.01));
        equationLabel.setHeight((int) (displayHeight * 0.05));
        ConstraintLayout.LayoutParams labelTextParams = (ConstraintLayout.LayoutParams) equationLabel.getLayoutParams();
        labelTextParams.topMargin = (int) (displayHeight * 0.03);
        equationLabel.setLayoutParams(labelTextParams);
    }

    public static void setEquationField(float displayHeight, int displayWidth, EditText equationInputField) {
        equationInputField.setWidth(displayWidth/2);
        equationInputField.setHeight((int) (displayHeight * 0.05));
        ConstraintLayout.LayoutParams textFieldParams = (ConstraintLayout.LayoutParams) equationInputField.getLayoutParams();
        textFieldParams.setMarginStart((int) (displayWidth * 0.02));
        textFieldParams.topMargin = (int) (displayHeight * 0.03);
        equationInputField.setLayoutParams(textFieldParams);
    }

    public static void setX_valueLabel(float displayHeight, TextView x_valueLabel) {
        x_valueLabel.setTextSize((int) (displayHeight * 0.01));
        x_valueLabel.setHeight((int) (displayHeight * 0.05));
        ConstraintLayout.LayoutParams x_valueLabelParams = (ConstraintLayout.LayoutParams) x_valueLabel.getLayoutParams();
        x_valueLabelParams.topMargin = (int) (displayHeight * 0.03);
        x_valueLabel.setLayoutParams(x_valueLabelParams);
    }

    public static void setX_valueInputField(float displayHeight, int displayWidth, EditText x_valueInputField) {
        x_valueInputField.setWidth(displayWidth/2);
        x_valueInputField.setHeight((int) (displayHeight * 0.05));
        ConstraintLayout.LayoutParams x_valueInputParams = (ConstraintLayout.LayoutParams) x_valueInputField.getLayoutParams();
        x_valueInputParams.setMarginStart((int) (displayWidth * 0.02));
        x_valueInputParams.topMargin = (int) (displayHeight * 0.03);
        x_valueInputField.setLayoutParams(x_valueInputParams);
    }

    public static void setResultHeader(float displayHeight, TextView resultHeader) {
        resultHeader.setTextSize(displayHeight * 0.01f);
        ConstraintLayout.LayoutParams resultHeaderParams = (ConstraintLayout.LayoutParams) resultHeader.getLayoutParams();
        resultHeaderParams.topMargin = (int) (displayHeight * 0.05f);
        resultHeader.setLayoutParams(resultHeaderParams);
    }

    public static void setResultText(float displayHeight, TextView resultText) {
        resultText.setTextSize(displayHeight * 0.008f);
        resultText.setHeight((int) (displayHeight * 0.3));
    }

    public static void setInputConfirmButton(float displayHeight, int displayWidth, Button inputConfirmButton) {
        inputConfirmButton.setWidth(displayWidth/3);
        inputConfirmButton.setHeight((int) (displayHeight/15));
        inputConfirmButton.setTextSize(displayHeight * 0.01f);
        ConstraintLayout.LayoutParams inputConfirmButtonParams = (ConstraintLayout.LayoutParams) inputConfirmButton.getLayoutParams();
        inputConfirmButtonParams.topMargin = (int) (displayHeight * 0.03);
        inputConfirmButton.setLayoutParams(inputConfirmButtonParams);
    }

    // sets the result of the apiRequest method to this observable
    static Observable<String> apiRequestObservable(String equation, String x_value) {
        return Observable.defer(new Supplier<ObservableSource<? extends String>>() {
            @Override public ObservableSource<? extends String> get() throws Throwable {
                // Do some long running operation
                String response = apiRequest(equation, x_value);
                return Observable.just(response);
            }
        });
    }

    // sends a server request to the server that processes the JSON formatted data
    public static String apiRequest(String equation, String x_value) {
        final String serverEndpoint = "https://autodyff.pythonanywhere.com/numerical_engine/endpoint";
        String errorReasoning = null;

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

            JSONObject resultJSON = new JSONObject(reader.readLine());
            errorReasoning = (String) resultJSON.get("error");

            return "The value of the normal function is: \n" + resultJSON.get("f")
                    + "\nThe value of the derivative is: \n" + resultJSON.get("f_prime"
                    + "\nErrors: \n" + errorReasoning);
        } catch (Exception e) {
            return "Error: " + e.getMessage();
        }
    }



    @Override
    public void onActivityCreated(@Nullable Bundle savedInstanceState) {
        super.onActivityCreated(savedInstanceState);
        mViewModel = new ViewModelProvider(this).get(HomeViewModel.class);
        // TODO: Use the ViewModel
    }

    @Override
    public void onDestroyView() {
        super.onDestroyView();
        disposables.clear();
    }
}