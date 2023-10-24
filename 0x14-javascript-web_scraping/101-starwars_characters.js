#!/usr/bin/node

const args = process.argv;
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${args[2]}`;

request(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    const moviesCharacters = JSON.parse(body).characters;

    const promises = moviesCharacters.map((character) => {
      return new Promise((resolve, reject) => {
        request(character, (error, response, body) => {
          if (error) reject(error);
          else resolve(JSON.parse(body).name);
        });
      });
    });

    Promise.all(promises).then((names) => {
      names.forEach((name) => {
        console.log(name);
      });
    });
  }
});
