import Foundation
import FoundationNetworking

// can use UIKit instead 

// define the URL endpoint of the web service

let url = URL(string: "https://www.codermerlin.academy/vapor/brennan-coil/numerical_engine/endpoint")!

// URL request object 
// mutable request 

var request = URLRequest(url: url)
request.httpMethod = "POST"

struct Message: Encodable {

   // let userID: Int
   // let toUserID: Int
    let equation: String
    let x: String

}

// encodable allows instance of struct to be converted to a Data object 

// create Message object 
// use JSONencoder instance to convert it to a Data object

let message = Message(
   // userID: 123,
   // toUserID: 456,
    equation: "x^2",
    x: "5"
)
let data = try! JSONEncoder().encode(message)

// try! operator to avoid dealing with optionals 

request.httpBody = data

// establish website as a JSON object

request.setValue(
    "application/json",
    forHTTPHeaderField: "Content-Type"
)


let task = URLSession.shared.dataTask(with: request) { data, response, error in
    let statusCode = (response as! HTTPURLResponse).statusCode
    print(statusCode)
    if statusCode == 200 {
        print("SUCCESS")
    } else {
        print("FAILURE")
    }
    // unwrap data safely 

    if let data = data {
    if let responseString = String(data: data, encoding: .utf8) {
        print("Response: \(responseString)")
    } else {
        print("Could not convert data to string")
    }
    } else {
        print("No data recieved")
    }
}

task.resume()
sleep(60)
