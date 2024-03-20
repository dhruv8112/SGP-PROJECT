
fetch("https://dhruvapi.vercel.app")
  .then((response) => response.json())
  .then((data) => {
    // Assuming data is an array of objects, each representing a row
    let rows = "";
    data.forEach((item) => {
      // Process each object to construct HTML rows
      rows += `<tr><td>${item.CMP_Rs}</td><td>${item.Name}</td></tr>`;
    });

    // Assuming you have a table element with id "api-data-table" in your HTML
    document.getElementById("tableRows").innerHTML = rows;
  })
  .catch((error) => console.log(error));
