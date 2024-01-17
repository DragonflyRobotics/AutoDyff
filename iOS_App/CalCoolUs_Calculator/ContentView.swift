//
//  ContentView.swift
//  CalCoolUs_Calculator
//
//  Created by Shivanshi Das on 12/15/23.
//

import SwiftUI

enum NumButton {
    // used as identifiers for buttons
    case one
    case two
    case three
    case four
    case five
    case six
    case seven
    case eight
    case nine
    case zero
    case add
    case subtract
    case divide
    case multiply
    case equal
    case clear
    case decimal
    case percent
    case negative
}

struct ContentView: View {
    
    let buttons: [[NumButton]] = [
        [.seven, .eight, .nine]
        ]
    var body: some View {
        ZStack { // layers overlap
            Color.black.edgesIgnoringSafeArea(.all)
            VStack {
                // Text display
                HStack {
                    Spacer()
                    // View expands to take up all available space along axis
                    Text("0")
                        .bold()
                        .font(.system(size:52))
                        .foregroundColor(.white)
                    
                    
                    // Buttons
                }
            }
            
        }
        
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
