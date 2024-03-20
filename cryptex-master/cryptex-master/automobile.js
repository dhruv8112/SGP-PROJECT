const axios = require('axios');

// Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
const apiKey = 'CDJQ1FBKMAN54A97';

// List of NSE automobile sector stock symbols
const automobileStockSymbols = ['M&M', 'TATAMOTORS', 'HEROMOTOCO'];

// Function to fetch real-time data for a stock
const fetchStockData = async (symbol) => {
  try {
    const quoteUrl = `https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=NSE:${symbol}&apikey=${apiKey}`;
    const quoteResponse = await axios.get(quoteUrl);
    const stockData = quoteResponse.data['Global Quote'];
    console.log('Stock Data for', symbol, ':', stockData);
    // Update HTML or perform further actions here
  } catch (error) {
    console.error('Error fetching stock data for', symbol, ':', error.message);
  }
};

// Fetch real-time data for each automobile sector stock
automobileStockSymbols.forEach(async (symbol) => {
  await fetchStockData(symbol);
});
