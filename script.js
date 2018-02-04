vowels = {'a': ['a', 'ā', 'á', 'ǎ', 'à'], 
          'e': ['e', 'ē', 'é', 'ě', 'è'],
          'i': ['i', 'ī', 'í', 'ǐ', 'ì'],
          'o': ['o', 'ō', 'ó', 'ǒ', 'ò'],
          'u': ['u', 'ū', 'ú', 'ǔ', 'ù'],
          'ü': ['ü', 'ǖ', 'ǘ', 'ǚ', 'ǜ']}

function pinyin(input) {
    var word = input.replace('v', 'ü');
    var punctuation = '';
    var tone = 0;

    var symbols = /[ !@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;

    while (symbols.test(word[word.length-1])) {
        punctuation += word[word.length-1]; 
        word = word.substr(0, word.length-1);
    }
    
    while (!isNaN(word[word.length-1])) {
        tone = Number(word[word.length-1]);
        word = word.substr(0, word.length-1);
        if (word.length <= 0)
            return input;
    } 

    vowel_to_change = '';
    if (word.indexOf('a') > -1)
        vowel_to_change = 'a';
    else if (word.indexOf('e') > -1)
        vowel_to_change = 'e';
    else if (word.indexOf('i') > -1)
        vowel_to_change = 'i';
    else if (word.indexOf('o') > -1)
        vowel_to_change = 'o';
    else if (word.indexOf('u') > -1)
        vowel_to_change = 'u';
    else if (word.indexOf('ü') > -1)
        vowel_to_change = 'ü';
    else 
        vowel_to_change = '';

    new_word = input;
    if (vowel_to_change)
        new_word = word.replace(vowel_to_change, vowels[vowel_to_change][tone]);
    return new_word + punctuation;
}

function convert(sentence) {
    var result = [];
    sentence = sentence.replace(/\n/g, " \n");
    words = sentence.split(' ');
    for (var i = 0; i < words.length; i++)
        result.push(pinyin(words[i], ''))

    return result.join(' ');
}

function trigger() {
    var sentences = document.getElementById("input").value
    document.getElementById("output").value = convert(sentences);
}
