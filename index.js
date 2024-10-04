const fetch = require('node-fetch');
const readlineSync = require('readline-sync');

console.log('Bem vindo ao Bot conversor 🤖💰');

async function robo() {
  const apiKey = '026009e18ee61f42839168c9'; // Sua chave da API
  const moedaBase = readlineSync.question('Informe uma moeda base (ex: USD): ') || 'USD';
  const moedaFinal = readlineSync.question('Informe uma moeda desejada (ex: BRL): ') || 'BRL';
  
  const url = `https://v6.exchangerate-api.com/v6/${apiKey}/latest/${moedaBase}`;
  
  try {
    const response = await fetch(url);
    const data = await response.json();
    
    if (data.result === 'success') {
      const rate = data.conversion_rates[moedaFinal];
      if (rate) {
        console.log(`O valor de 1 ${moedaBase} em ${moedaFinal} é ${rate}`);
      } else {
        console.log(`Não foi possível obter a taxa de conversão para ${moedaFinal}.`);
      }
    } else {
      console.log('Erro ao obter os dados de conversão:', data['error-type']);
    }
  } catch (error) {
    console.error('Erro ao executar o robô:', error);
  }
}

robo();


