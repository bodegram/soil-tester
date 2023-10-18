let cardOne = document.getElementById('cardOne')
let cardTwo = document.getElementById('cardTwo')

cardTwo.classList.add('card-disable')

cardOne.addEventListener('click', ()=>{
    cardOne.classList.remove('card-disable')
    cardTwo.classList.add('card-disable')
})

cardTwo.addEventListener('click', ()=>{
    cardOne.classList.add('card-disable')
    cardTwo.classList.remove('card-disable')
})