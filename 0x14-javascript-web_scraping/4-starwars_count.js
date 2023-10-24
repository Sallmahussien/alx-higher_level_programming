#!/usr/bin/node

const args = process.argv;
const request = require('request');

request(args[2], (error, response, body) => {
  if (!error) {
    let moviesCount = 0;
    const moviesData = JSON.parse(body).results;

    moviesData.forEach((movie) => {
      movie.characters.forEach((character) => {
        if (character.endsWith('/18/')) moviesCount++;
      });
    });

    console.log(moviesCount);
  }
});
