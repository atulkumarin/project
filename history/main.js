d3.json(word2vecFile, function (error, data) {
    console.log("hey");
    console.log(filterWords(data, 'speaking'))
});