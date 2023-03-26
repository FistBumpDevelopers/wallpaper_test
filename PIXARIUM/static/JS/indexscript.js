/*Hover images*/
const clip = document.querySelectorAll('.clip');
for(let i=0; i<clip.length; i++){
    clip[i].addEventListener('mouseenter',
    function(x){
        clip[i].play()
    })
    clip[i].addEventListener('mouseout',
    function(x){
        clip[i].pause();
    })
}

/*search bar*/
const input = document.getElementById("search-id");
const val=input.value;
input.addEventListener("mouseenter", function(){
    input.classList.remove("search-bar");
    input.classList.add("select-search");
    this.placeholder="";
})
// onblur
input.addEventListener("mouseout", function(){
    input.classList.add("search-bar");
    input.classList.remove("select-search");
        this.placeholder="Rummage here...";
})

input.addEventListener("keypress", (e)=>{
    if(e.key==='Enter' && input.value.length>0){
    input.addEventListener("click")
    console.log(input.value); //inga than da mathanum... nee enna pannanumo pannika inga... inga podrathu enter amukuna trigger agum
    input.value="";
    }
})
/*cursor*/


const cursor = document.getElementById("cursor");

document.addEventListener("mousemove", (e) =>{
    cursor.style.left = e.clientX + "px";
    cursor.style.top = e.clientY + "px";
});


// Parallax
let layer10= document.getElementById("layer-10");
let layer9 = document.getElementById("layer-9");
let layer8 = document.getElementById("layer-8");
let layer7 = document.getElementById("layer-7");
let layer6 = document.getElementById("layer-6");
let layer4 = document.getElementById("layer-4");
let layer3 = document.getElementById("layer-3");
let layer2 = document.getElementById("layer-2");

window.addEventListener("scroll", ()=>{
  let value=window.scrollY;

  layer10.style.left = value * 1.5 + "px";
    layer9.style.left = value * -0.5 + "px";
    layer8.style.left = value * 0.5 + "px";
    layer7.style.left = value * -1.5 + "px";
  layer6.style.left = value * 1 + "px";
    layer4.style.opacity = value/(value+50);
    layer3.style.transformOrigin = "center";
    layer3.style.transform = 'rotate(' + value + 'deg)';

})