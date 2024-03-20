// fetch("https://dhruvapi.vercel.app/").then((response) => {
//   if (response.ok) {
//     return response.json(); // Parse the JSON response
//   }
//   throw new Error("Network response was not ok.");
// });
fetch("https://dhruvapi.vercel.app/")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  })
  .then((res) => {
    const data = res;
    let rows = "";
    data.forEach((item) => {
      rows += `<tr>
                        <td>${item["S.No."]}</td>
                        <td>${item["Name"]}</td>
                        <td>${item["CMP Rs. "]}</td>
                        <td>${item["Mar Cap Rs.Cr. "]}</td>
                        <td>${item["NP Qtr Rs.Cr. "]}</td>
                        <td>${item["Div Yld % "]}</td>
                        <td>${item["P/E "]}</td>
                        <td>${item["Qtr Profit Var % "]}</td>
                        <td>${item["Qtr Sales Var % "]}</td>
                        <td>${item["Sales Qtr Rs.Cr. "]}</td>
                        <td>${item["Piotski Scr "]}</td>
                        <td>${item["ROCE % "]}</td>
                    </tr>`;
    });
    console.log(rows);
    document.getElementById("tableBody").innerHTML = rows;
  })
  .catch((error) =>
    console.error("There was a problem with the fetch operation:", error)
  );
