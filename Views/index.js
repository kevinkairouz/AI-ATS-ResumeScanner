function findFit() {
    const file = document.getElementById("resumeInput").files[0];
    if (!file) {
        console.log("No file selected");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    fetch("http://127.0.0.1:5000/uploadResume", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.log("Something went wrong");
    });
}
