const word2vecFile = 'figures/word2vec.json';


d3.json(word2vecFile, function (error, data) {
    console.log("hey");
    console.log(data['speaking'])
});