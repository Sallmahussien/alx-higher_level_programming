#!/usr/bin/node

const args = process.argv;
const request = require('request');

const characterURL = 'https://swapi-api.alx-tools.com/api/people/18/';

request(args[2], (error, response, body) => {
  if (error) console.log(error);
  else {
    let moviesCount = 0;
    const moviesData = JSON.parse(body).results;

    moviesData.forEach((movie) => {
      if (movie.characters.includes(characterURL)) moviesCount++;
    });

    console.log(moviesCount);
  }
});
