const player1 = document.querySelector("#player1")
const player2 = document.querySelector("#player2")
const result = document.querySelector("#result")
const choiceBtn = document.querySelectorAll(".choiceBtn")

let player1Value
let player2Value
let resultValue

choiceBtn.forEach(button => button.addEventListener("click",() =>{

  player1Value = button.textContent
  player2turn()
  player1.textContent = `Player1: ${player1Value}`
  player2.textContent = `Player2: ${player2Value}`
  result.textContent = checkWinner()



}))

function player2turn(){
  const randNum = Math.floor(Math.random()*3) + 1

  // console.log(randNum)

  switch(randNum){
    case 1:
      player2Value = "Rock"
      break
    case 2:
      player2Value = "Paper"
      break
    case 3:
      player2Value = "Scissor"
      break
  }
}

function checkWinner (){
  if(player1Value == player2Value){
    return `Draw!`
  }else if(player2Value == "Rock"){
    return (player1Value == "Paper") ? "You win!" : "You lose!"
  }else if(player2Value == "Paper"){
    return (player1Value == "Scissor") ? "You win!" : "You lose!"
  }else if(player2Value == "Scissor"){
    return (player1Value == "Rock") ? "You win!" : "You lose!"
  }
}