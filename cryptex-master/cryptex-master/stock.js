const axios = require('axios');

// Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
var apiKey = 'CDJQ1FBKMAN54A97';
var url = `https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey=${apiKey}`;

axios.get(url)
  .then(response => {
    const data = response.data;
    console.log(data); // Log the entire data object

    // Check if data contains the expected structure
    if (data && data['Gainers'] && data['Losers']) {
      // Extracting data for top gainers
      var topGainers = data['Gainers'];
      console.log('Top Gainers:');
      topGainers.forEach(gainer => {
        console.log(gainer['symbol'], gainer['price'], gainer['changesPercentage']);
      });

      // Extracting data for top losers
      var topLosers = data['Losers'];
      console.log('Top Losers:');
      topLosers.forEach(loser => {
        console.log(loser['symbol'], loser['price'], loser['changesPercentage']);
      });
    } else {
      console.error('Unexpected data structure:', data);
    }
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
