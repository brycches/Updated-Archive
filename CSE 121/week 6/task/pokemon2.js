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
            //console.log(response.json)
            return response.json();
        })
        .then(data => {
            fetchPokemonTypeData(data);
            //console.log(data)
            // fetchMoveData(data)
        })
        .catch(error => {
            displayError(error);
        });
}

function fetchPokemonTypeData(data) {
    let pokemonType = null
    let pokemonType1 = null
    let pokemonType2 = null

    if (data.types.length === 1)
    { pokemonType = data.types[0].type.name
    //console.log(pokemonType)}
    }
    else if (data.types.length === 2){
        pokemonType1 = data.types[0].type.name;
        pokemonType2 = data.types[1].type.name;
    }
    const allTypes = [
        'Normal',
        'Fire',
        'Water',
        'Electric',
        'Grass',
        'Ice',
        'Fighting',
        'Poison',
        'Ground',
        'Flying',
        'Psychic',
        'Bug',
        'Rock',
        'Ghost',
        'Steel',
        'Dragon',
        'Dark',
        'Fairy'
    ];
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
    let weakness = ''
    let neutral = ''
    let strengths = ''
    let immunities = ''
    let typeError = ''
    let numbers = 0
    let combinedChart = {}
    //const allTypes = [
        //'normal', 'fire', 'water', 'electric', 'grass', 'ice', 'fighting', 'poison', 'ground', 'flying', 'psychic', 'bug', 'rock', 'ghost', 'steel', 'dragon', 'dark', 'fairy'
        //];
    for (const type in typeChart) {
        if (pokemonType === type)
        {
            let typeEffectiveness = typeChart[type];
            //console.log('typeEffectiveness', typeEffectiveness);
            for (const effectiveness in typeEffectiveness)
            {
                //console.log('effectiveness', effectiveness)
                //console.log(effectiveness)
                if (typeEffectiveness[effectiveness] > 1)
                {
                    let why = `${effectiveness} `
                    //console.log('weakness', why)

                    weakness += `${effectiveness}, `
                }
                else if (typeEffectiveness[effectiveness] === 1)
                {
                    neutral += `${effectiveness}, `
                }
                else if (typeEffectiveness[effectiveness] < 1 && typeEffectiveness[effectiveness] > 0)
                {
                    strengths += `${effectiveness}, `
                }
                else if (typeEffectiveness[effectiveness] == 0)
                {
                    immunities += `${effectiveness}, `
                }
                else
                {
                    typeError += `\nThere was an error determining the effectiveness of ${effectiveness}. `                
                }
            }
        }
        else if (pokemonType1 === type)
        {
            let typeEffectiveness1 = []
            typeEffectiveness1 = typeChart[pokemonType1]
            //console.log(typeEffectiveness1)
            let typeEffectiveness2 = []
            typeEffectiveness2 = typeChart[pokemonType2]
            //console.log(typeEffectiveness2)
            for (const typeName in typeEffectiveness1)
                {
                    //console.log('typeName', typeName)
                    numbers += 1
                    //console.log('numbers', numbers)
                    //console.log('allTypes', allTypes[numbers])
                    //console.log(typeEffectiveness1['Fire'])
                    //console.log('typeEffectiveness1[allTypes[numbers]]', typeEffectiveness1[allTypes[numbers]])
                    //console.log('typeEffectiveness1[numbers]', typeEffectiveness1[allTypes[numbers]])
                    let firstone = parseFloat(typeEffectiveness1[typeName]);
                    //console.log(firstone)
                    let secondOne = parseFloat(typeEffectiveness2[typeName])
                    //console.log(firstone+secondOne)
                    if (parseFloat(typeEffectiveness1[typeName]) != 0 && parseFloat(typeEffectiveness2[typeName]) != 0)
                    {
                        combinedChart[typeName] = parseFloat(typeEffectiveness1[typeName]) + parseFloat(typeEffectiveness2[typeName]);
                        //console.log('combined chart', combinedChart)
                    } 
                    else
                    {
                        combinedChart[typeName] = 0
                    }
                }

            //console.log('typeEffectiveness1', typeEffectiveness1, 'typeEffectiveness2', typeEffectiveness2 )
            for (const effectiveness in combinedChart)
            {
                //console.log('effectiveness', effectiveness)
                //console.log(effectiveness)
                if (combinedChart[effectiveness] > 2.5)
                {
                    let why = `${effectiveness} `
                    //console.log('weakness', why)

                    weakness += `${effectiveness}, `
                }
                else if (combinedChart[effectiveness] === 2 || combinedChart[effectiveness] === 2.5)
                {
                    neutral += `${effectiveness}, `
                }
                else if (combinedChart[effectiveness] < 2 && combinedChart[effectiveness] > 0)
                {
                    strengths += `${effectiveness}, `
                }
                else if (combinedChart[effectiveness] === 0)
                {
                    immunities += `${effectiveness}, `
                }
                else
                {
                    typeError += `\nThere was an error determining the effectiveness of ${effectiveness}. `                
                }
            }
        }





    };
    const resultElement = document.getElementById('result');
    resultElement.innerHTML = `<p>Pokemon defenses</p> <p>Resistant to: ${strengths}</p> <p>Neutral against: ${neutral}</p> <p>Weak against: ${weakness}</p>`;
    if (immunities != ''){
        resultElement.innerHTML += `<p>Immunities: ${immunities}</p>`
    }
    if (typeError != ''){
        resultElement.innerHTML += `<p>${typeError}</p>`
    }
}

// function fetchMoveData(data)
// {

//     const length = data.moves.length
//     for (let i = 0; i < length; i++)
//     {
//         const moveDataUrl = data.moves[i].move.url;
//         const fetchAndProcessData = async () => {
//         try {
//             const response = await fetch(moveDataUrl);
            
//             if (!response.ok) {
//               throw new Error(`Move not found: ${response.status}`);
//             }
      
//             const moveData = await response.json();
      
//             // Access and process moveData here
//             //console.log("Move data for move " + i + ":", moveData);

//             //console.log(moveData.type.name)
//             let moveInfo = moveData
//             //console.log('moveInfo', moveInfo)
//             resultElement.innerHTML += `<h3>Move: ${moveInfo.name}</h3>`;
//                         resultElement.innerHTML += `<p>Type: ${moveInfo.type.name}</p>`;
//                         resultElement.innerHTML += `<p>Damage Class: ${moveInfo.damageClass.name}</p>`;
//                         resultElement.innerHTML += `<p>Power: ${moveInfo.power || 'N/A'}</p>`;
//                         resultElement.innerHTML += `<p>Accuracy: ${moveInfo.accuracy || 'N/A'}</p>`;

//                         // Check if effectEntries is not empty before accessing short_effect
//                         if (moveInfo.effectEntries.length > 0) {
//                             resultElement.innerHTML += `<p>Effect: ${moveInfo.effectEntries[0].short_effect || 'N/A'}</p>`;
//                         } else {
//                             resultElement.innerHTML += `<p>Effect: N/A</p>`;
//                         }

//                         resultElement.innerHTML += `<p>${determineEffectiveness(moveInfo.type)}</p>`
//                         resultElement.innerHTML += `<hr>`; 










//                 }




//         catch (error) {
//             console.error("Error fetching move data: " + error);
//           }

//         }
//         fetchAndProcessData()
//     };
        
    






    
// };


    



// function determineEffectiveness(moveType)
// {
//     let weakness = ''
//     let neutral = ''
//     let strengths = ''
//     let immunities = ''
//     let typeError = ''
//     for (const type in typeChart) {
//         if (moveType === type)
//         {
//             let typeEffectiveness = typeChart[type];
//             //console.log('typeEffectiveness', typeEffectiveness);
//             for (const effectiveness in typeEffectiveness)
//             {
//                 //console.log('effectiveness', effectiveness)
//                 //console.log(effectiveness)
//                 if (typeEffectiveness[effectiveness] > 1)
//                 {
//                     let why = `${effectiveness} `
//                     //console.log('weakness', why)

//                     weakness += `${effectiveness}, `
//                 }
//                 else if (typeEffectiveness[effectiveness] === 1)
//                 {
//                     neutral += `${effectiveness}, `
//                 }
//                 else if (typeEffectiveness[effectiveness] < 1 && typeEffectiveness[effectiveness] > 0)
//                 {
//                     strengths += `${effectiveness}, `
//                 }
//                 else if (typeEffectiveness[effectiveness] == 0)
//                 {
//                     immunities += `${effectiveness}, `
//                 }
//                 else
//                 {
//                     typeError += `\nThere was an error determining the effectiveness of ${effectiveness}. `                
//                 }
//             }
//         }
//     }
// }




function displayError(error) {
    const resultElement = document.getElementById('result');
    resultElement.innerHTML = `<p>Error: ${error.message}</p>`;
}

fetchPokemonData()



