let typeChart = {
    normal: {
        Bug: 1, Dark: 1, Dragon: 1, Electric: 1, Fairy: 1, Fighting: 2, Fire: 1, Flying: 1, Ghost: 0, Grass: 1, Ground: 1, Ice: 1, Normal: 1, Poison: 1, Psychic: 1, Rock: 1, Steel: 1, Water: 1
    },
    fire: {
        Bug: 0.5, Dark: 1, Dragon: 1, Electric: 1, Fairy: 0.5, Fighting: 1, Fire: 0.5, Flying: 1, Ghost: 1, Grass: 0.5, Ground: 2, Ice: 0.5, Normal: 1, Poison: 1, Psychic: 1, Rock: 2, Steel: 0.5, Water: 2
    },
    water: {
        Bug: 1, Dark: 1, Dragon: 1, Electric: 2, Fairy: 1, Fighting: 1, Fire: 0.5, Flying: 1, Ghost: 1, Grass: 2, Ground: 1, Ice: 0.5, Normal: 1, Poison: 1, Psychic: 1, Rock: 1, Steel: 0.5, Water: 0.5
    },
    electric: {
        Bug: 1, Dark: 1, Dragon: 1, Electric: 0.5, Fairy: 1, Fighting: 1, Fire: 1, Flying: 0.5, Ghost: 1, Grass: 1, Ground: 2, Ice: 1, Normal: 1, Poison: 1, Psychic: 1, Rock: 1, Steel: 0.5, Water: 1
    },
    grass: {
        Bug: 2, Dark: 1, Dragon: 1, Electric: 0.5, Fairy: 1, Fighting: 1, Fire: 2, Flying: 2, Ghost: 1, Grass: 0.5, Ground: 0.5, Ice: 2, Normal: 1, Poison: 2, Psychic: 1, Rock: 1, Steel: 1, Water: 0.5 
    },
    ice: {
        Bug: 1, Dark: 1, Dragon: 1, Electric: 1, Fairy: 1, Fighting: 2, Fire: 2, Flying: 1, Ghost: 1, Grass: 1, Ground: 1, Ice: 0.5, Normal: 1, Poison: 1, Psychic: 1, Rock: 2, Steel: 2, Water: 1
    },
    fighting: {
        Bug: 0.5, Dark: 0.5, Dragon: 1, Electric: 1, Fairy: 2, Fighting: 1, Fire: 1, Flying: 2, Ghost: 1, Grass: 1, Ground: 1, Ice: 1, Normal: 1, Poison: 1, Psychic: 2, Rock: 0.5, Steel: 1, Water: 1
    },
    poison: {
        nBug: 0.5, Dark: 1, Dragon: 1, Electric: 1, Fairy: 0.5, Fighting: 0.5, Fire: 1, Flying: 1, Ghost: 1, Grass: 0.5, Ground: 2, Ice: 1, Normal: 1, Poison: 0.5, Psychic: 2, Rock: 1, Steel: 1, Water: 1
    },
    ground: {
        Bug: 1, Dark: 1, Dragon: 1, Electric: 0, Fairy: 1, Fighting: 1, Fire: 1, Flying: 1, Ghost: 1, Grass: 2, Ground: 1, Ice: 2, Normal: 1, Poison: 0.5, Psychic: 1, Rock: 0.5, Steel: 1, Water: 2
    },
    flying: {
        Bug: 0.5, Dark: 1, Dragon: 1, Electric: 2, Fairy: 1, Fighting: 0.5, Fire: 1, Flying: 1, Ghost: 1, Grass: 0.5, Ground: 0, Ice: 2, Normal: 1, Poison: 1, Psychic: 1, Rock: 2, Steel: 1, Water: 1
    },
    psychic: {
        Bug: 2, Dark: 2, Dragon: 1, Electric: 1, Fairy: 1, Fighting: 0.5, Fire: 1, Flying: 1, Ghost: 2, Grass: 1, Ground: 1, Ice: 1, Normal: 1, Poison: 1, Psychic: 0.5, Rock: 1, Steel: 1, Water: 1
    },
    bug: {
        Bug: 1, Dark: 1, Dragon: 1, Electric: 1, Fairy: 1, Fighting: 0.5, Fire: 2, Flying: 2, Ghost: 1, Grass: 0.5, Ground: 0.5, Ice: 1, Normal: 1, Poison: 1, Psychic: 1, Rock: 2, Steel: 1, Water: 1
    },
    rock: {
        Bug: 1, Dark: 1, Dragon: 1, Electric: 1, Fairy: 1, Fighting: 2, Fire: 0.5, Flying: 0.5, Ghost: 1, Grass: 2, Ground: 2, Ice: 1, Normal: 0.5, Poison: 0.5, Psychic: 1, Rock: 1, Steel: 2, Water: 2
    },
    ghost: {
        Bug: 0.5, Dark: 2, Dragon: 1, Electric: 1, Fairy: 1, Fighting: 0, Fire: 1, Flying: 1, Ghost: 2, Grass: 1, Ground: 1, Ice: 1, Normal: 0, Poison: 0.5, Psychic: 1, Rock: 1, Steel: 1, Water: 1 
    },
    steel: {
        Bug: 0.5, Dark: 1, Dragon: 0.5, Electric: 1, Fairy: 0.5, Fighting: 2, Fire: 2, Flying: 0.5, Ghost: 1, Grass: 0.5, Ground: 2, Ice: 0.5, Normal: 0.5, Poison: 0, Psychic: 0.5, Rock: 0.5, Steel: 0.5, Water: 1
    },
    dragon: {
        Bug: 1, Dark: 1, Dragon: 2, Electric: 0.5, Fairy: 2, Fighting: 1, Fire: 0.5, Flying: 1, Ghost: 1, Grass: 0.5, Ground: 1, Ice: 2, Normal: 1, Poison: 1, Psychic: 1, Rock: 1, Steel: 1, Water: 0.5
    },
    dark: {
        Bug: 2, Dark: 0.5, Dragon: 1, Electric: 1, Fairy: 2, Fighting: 2, Fire: 1, Flying: 1, Ghost: 0.5, Grass: 1, Ground: 1, Ice: 1, Normal: 1, Poison: 1, Psychic: 0, Rock: 1, Steel: 1, Water: 1
    },
    fairy: {
        Bug: 0.5, Dark: 0.5, Dragon: 0, Electric: 1, Fairy: 1, Fighting: 0.5, Fire: 1, Flying: 1, Ghost: 1, Grass: 1, Ground: 1, Ice: 1, Normal: 1, Poison: 2, Psychic: 1, Rock: 1, Steel: 2, Water: 1
    },
}



function fetchPokemonData() {
    const inputElement = document.getElementById('pokemonName');
    let pokemonName = inputElement.value.toLowerCase();

    // Check if the input is empty, and provide a default value if it is
    if (pokemonName === '') {
        pokemonName = 'pikachu'; // You can set any default name you prefer
        inputElement.value = pokemonName; // Update the input field to show the default name
    }

    const apiUrl = `https://pokeapi.co/api/v2/pokemon/${pokemonName}/`;
    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Pokemon not found: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            fetchPokemonTypeData(data);
            console.log(data)
        })
        .catch(error => {
            displayError(error);
        });
}

function fetchPokemonTypeData(data) {
    let weaknesses = new Set();
    let neutral = new Set();
    let strengths = new Set();
    let immunities = new Set();
    let typeErrors = new Set();

    for (let i = 0; i < data.types.length; i++) {
        const typeName = data.types[i].type.name;
        const typeEffectiveness = typeChart[typeName];

        if (typeEffectiveness) {
            for (const effectiveness in typeEffectiveness) {
                if (typeEffectiveness[effectiveness] > 1) {
                    weaknesses.add(effectiveness);
                } else if (typeEffectiveness[effectiveness] === 1) {
                    neutral.add(effectiveness);
                } else if (typeEffectiveness[effectiveness] < 1 && typeEffectiveness[effectiveness] > 0) {
                    strengths.add(effectiveness);
                } else if (typeEffectiveness[effectiveness] === 0) {
                    immunities.add(effectiveness);
                } else {
                    typeErrors.add(`There was an error determining the effectiveness of ${effectiveness}.`);
                }
            }
        } else {
            typeErrors.add(`Type not found in the type chart: ${typeName}.`);
        }
    }

    const resultElement = document.getElementById('result');
    resultElement.innerHTML = '<p>Pokemon defenses</p>';
    
    if (strengths.size > 0) {
        resultElement.innerHTML += `<p>Resistant to: ${[...strengths].join(', ')}</p>`;
    }

    if (neutral.size > 0) {
        resultElement.innerHTML += `<p>Neutral against: ${[...neutral].join(', ')}</p>`;
    }

    if (weaknesses.size > 0) {
        resultElement.innerHTML += `<p>Weak against: ${[...weaknesses].join(', ')}</p>`;
    }

    if (immunities.size > 0) {
        resultElement.innerHTML += `<p>Immunities: ${[...immunities].join(', ')}</p>`;
    }

    if (typeErrors.size > 0) {
        resultElement.innerHTML += `<p>${[...typeErrors].join(' ')}</p>`;
    }
}
function displayError(error) {
    const resultElement = document.getElementById('result');
    resultElement.innerHTML = `<p>Error: ${error.message}</p>`;
}

fetchPokemonData()
