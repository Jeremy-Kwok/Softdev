//
//  ContentView.swift
//  TedX Demo
//
//  Created by Jeremy Kwok on 3/23/23.
//

import SwiftUI

struct ContentView: View {
    @StateObject var gameState = GameState()
    
    var body: some View {
        
        let borderSize = CGFloat(5)
        
        //whose turn is it?
        Text(gameState.turnText())
            .font(.title)
            .bold()
            .padding()
        
        Spacer()
        
        //Cross Player Score
        Text(String(format: "Crosses: %d", gameState.crossesScore))
            .font(.title)
            .bold()
            .padding()
        
        VStack(spacing: borderSize) {
            ForEach(0...2, id: \.self) {
                row in
                
                HStack(spacing: borderSize) {
                    ForEach(0...2, id: \.self) {
                        column in
                        
                        let cell = gameState.board[row][column]
                        
                        Text(cell.displayTile())
                            //Modifiers
                            .font(.system(size: 60))
                            .foregroundColor(cell.tileColor())
                            .bold()
                            .frame(maxWidth: .infinity, maxHeight: .infinity)
                            //width = height, fit to enlarge as much as the screen allows it to
                            .aspectRatio(1, contentMode: .fit)
                            .background(Color.white)
                            .onTapGesture {
                                gameState.placeTile(row, column)
                            }
                    }
                }
                
            }
        }
        .background(Color.black)
        .padding()
        .alert(isPresented: $gameState.showAlert) {
            Alert(
                title: Text(gameState.alertMessage),
                dismissButton: .default(Text("Okay"))
                {
                    gameState.resetBoard()
                }
            )
        }
        
        //Circle Player Score
        Text(String(format: "Circles: %d", gameState.circlesScore))
            .font(.title)
            .bold()
            .padding()
        
        Spacer()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
