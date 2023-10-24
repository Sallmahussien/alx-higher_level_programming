#!/usr/bin/node

const args = process.argv;
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${args[2]}`;

request(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    const moviesCharacters = JSON.parse(body).characters;

    moviesCharacters.forEach((character) => {
      request(character, (error, response, body) => {
        if (error) console.log(error);
        else console.log(JSON.parse(body).name);
      });
    });
  }
});
