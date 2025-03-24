const btn = document.getElementById("check-btn");
const input = document.getElementById("text-input");
const result=document.getElementById("result");

const isInputWritten = (input) => {
    if (input === "") {
        alert("Please input a value");
    }
}


btn.addEventListener("click", () => {
    isInputWritten(input.value);
result.innerText=`${input.value} is a chuthiya`;
   
});
