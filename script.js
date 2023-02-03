// // Elements
const passwordBox = document.querySelector('.main-textbox')
const btn = document.querySelector('.btn')
const rangeSlider = document.querySelector('#range')
const checkboxUppercase = document.querySelector('#checkbox1')
const checkboxLowercase = document.querySelector('#checkbox2')
const checkboxSpecialChar = document.querySelector('#checkbox3')
const visibleIcon = document.querySelector('#icon')
const passwordResult = document.querySelector('.password-result')
const output = document.querySelector('#output')

let value = rangeSlider.valueAsNumber

rangeSlider.addEventListener('wheel', (e) => {
    if (e.deltaY >= 8) {
        value += 1;
        output.innerHTML = value += 1
        
    } 
    if (e.deltaY <= 14) {
        value -= 1;
        output.innerHTML = value -= 1
    }

    e.preventDefault()
    e.stopPropagation()   
})


