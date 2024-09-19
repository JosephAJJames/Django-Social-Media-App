console.log("hello, world!");



var new_post_button = document.getElementById("New-post")
console.log(new_post_button);

var new_post_button_div = document.getElementById("New-post-div")
console.log(new_post_button_div);



new_post_button.addEventListener("click", () => {
    var new_post_button_div = document.getElementById("New-post-div")

    console.log("chebs");

    if (new_post_button_div.classList.contains("New-post-div-hidden")) {

        new_post_button_div.classList.replace("New-post-div-hidden", "New-post-div-shown");

    } else if (new_post_button_div.classList.contains("New-post-div-shown")) {

        new_post_button_div.classList.replace("New-post-div-shown", "New-post-div-hidden");
    }
})