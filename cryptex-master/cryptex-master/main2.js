// // Fetch data from the API
// async function fetchData() {
//   try {
//     const response = await fetch("https://dhruvapi.vercel.app");
//     const data = await response.json();

//     // Populate dropdown list
//     const selectElement = document.getElementById("item-select");
//     selectElement.innerHTML = ""; // Clear previous options

//     data.forEach((item) => {
//       const option = document.createElement("option");
//       option.value = item.Name; // Set option value to the name
//       option.textContent = item.Name; // Display 'Name' in the dropdown
//       selectElement.appendChild(option);
//     });

//     // Display default details
//     if (data.length > 0) {
//       displayDetails(data[0]); // Display details of the first item by default
//     }
//   } catch (error) {
//     console.error("Error fetching data:", error);
//   }
// }

// // Display details in the table based on the selected item
// function displayDetails(selectedItem) {
//   const table = document.getElementById("detail-table");
//   table.innerHTML = ""; // Clear previous table content

//   // Create table header
//   const thead = document.createElement("thead");
//   const headerRow = document.createElement("tr");
//   ["CMP_Rs", "Name", "PE"].forEach((columnName) => {
//     const th = document.createElement("th");
//     th.textContent = columnName;
//     headerRow.appendChild(th);
//   });
//   thead.appendChild(headerRow);
//   table.appendChild(thead);

//   // Create table body
//   const tbody = document.createElement("tbody");
//   const bodyRow = document.createElement("tr");
//   ["CMP_Rs", "Name", "PE"].forEach((columnName) => {
//     const td = document.createElement("td");
//     td.textContent = selectedItem[columnName];
//     bodyRow.appendChild(td);
//   });
//   tbody.appendChild(bodyRow);
//   table.appendChild(tbody);
// }

// // Event listener for dropdown selection change
// document.getElementById("item-select").addEventListener("change", function () {
//   const selectedName = this.value;
//   const selectedItem = data.find((item) => item.Name === selectedName); // Assuming 'data' contains fetched API data
//   displayDetails(selectedItem);
// });

// // Initial data fetch when the page loads
// fetchData();

//  from here it Is new  Code
// let apiData = []; // Variable to store fetched API data

// // Fetch data from the API
// async function fetchData() {
//     try {
//         const response = await fetch("https://dhruvapi.vercel.app");
//         apiData = await response.json();

//         // Populate dropdown list
//         const selectElement = document.getElementById('item-select');
//         selectElement.innerHTML = ''; // Clear previous options

//         apiData.forEach(item => {
//             const option = document.createElement('option');
//             option.value = item.Name; // Set option value to the name
//             option.textContent = item.Name; // Display 'Name' in the dropdown
//             selectElement.appendChild(option);
//         });

//         // Display details of the first item by default
//         if (apiData.length > 0) {
//             displayDetails(apiData[0]);
//         }
//     } catch (error) {
//         console.error('Error fetching data:', error);
//     }
// }

// // Display details in the table based on the selected item
// function displayDetails(selectedItem) {
//     const table = document.getElementById('detail-table');
//     table.innerHTML = ''; // Clear previous table content

//     // Create table header
//     const thead = document.createElement('thead');
//     const headerRow = document.createElement('tr');
//     ['CMP_Rs', 'Name', 'PE'].forEach(columnName => {
//         const th = document.createElement('th');
//         th.textContent = columnName;
//         headerRow.appendChild(th);
//     });
//     thead.appendChild(headerRow);
//     table.appendChild(thead);

//     // Create table body
//     const tbody = document.createElement('tbody');
//     const bodyRow = document.createElement('tr');
//     ['CMP_Rs', 'Name', 'PE'].forEach(columnName => {
//         const td = document.createElement('td');
//         td.textContent = selectedItem[columnName];
//         bodyRow.appendChild(td);
//     });
//     tbody.appendChild(bodyRow);
//     table.appendChild(tbody);
// }

// // Event listener for dropdown selection change
// document.addEventListener('DOMContentLoaded', async () => {
//     await fetchData(); // Wait for data to be fetched
//     const selectElement = document.getElementById('item-select');
//     selectElement.addEventListener('change', function() {
//         const selectedIndex = this.selectedIndex;
//         if (selectedIndex >= 0) {
//             const selectedItem = apiData[selectedIndex];
//             displayDetails(selectedItem);
//         }
//     });
// });

$(document).ready(function () {
  // Function to fetch data from API and populate dropdown
  function populateDropdown() {
    $.get("https://dhruvapi.vercel.app", function (data) {
      data.forEach(function (item) {
        $("#dropdown").append(
          `<option value="${item.Name}">${item.Name}</option>`
        );
      });
    });
  }

  // Call the populateDropdown function to initially populate the dropdown
  populateDropdown();

  // Show details when button is clicked
  $("#showDetails").on("click", function () {
    var selectedName = $("#dropdown").val();
    $.get("https://dhruvapi.vercel.app", function (data) {
      var selectedDetails = data.find(function (item) {
        return item.Name === selectedName;
      });
      if (selectedDetails) {
        // Append a new row to the table with the selected item's details
        $("#detailsTable tbody").append(
          `<tr><td>${selectedDetails.Name}</td><td>${selectedDetails.CMP_Rs}</td><td>${selectedDetails.PE}</td></tr>`
        );
      } else {
        alert("Details not found for the selected item.");
      }
    });
  });
});
