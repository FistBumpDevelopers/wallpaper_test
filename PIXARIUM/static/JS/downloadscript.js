let downloadBtn = document.querySelector("button");
let imageURL = document.querySelector("img").getAttribute("src");

downloadBtn.addEventListener(
  "click",
  (fun = () => {
    toDataURL(imageURL);
  })
);

function toDataURL(url) {
  fetch(url)
    .then((response) => response.blob())
    .then((file) => {
      let tempURL = URL.createObjectURL(file);
      let a = document.createElement("a");
      a.href = tempURL;
      a.download = "Download";
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(tempURL);
    });
}
