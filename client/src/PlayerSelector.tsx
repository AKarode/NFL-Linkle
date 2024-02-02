import React, { useState } from 'react';
import playersData from '../../teammate_map_1997-2018.json';

type Player = {
    name: string;
};

const PlayerSelector: React.FC = () => {
    const [searchTerm, setSearchTerm] = useState('');

    const playersArray = Object.keys(playersData).map(fullName => {
        const name = fullName.split(' (')[0]; // Split the string to separate the name from the college
        return { name };
    });

    const [players, setPlayers] = useState<Player[]>(playersArray);

    const filteredPlayers = players.filter(player =>
        player.name.toLowerCase().includes(searchTerm.toLowerCase())
    );

    // Example click handler for player button
    const handlePlayerClick = (playerName: string) => {
        console.log(playerName + ' button clicked');
        // Implement any action you want to take when a player button is clicked
    };

    return (
        <div>
            <input 
                type="text" 
                placeholder="Search Players" 
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
            />
            <div style={{ maxHeight: '300px', overflowY: 'auto', marginTop: '10px' }}>
                <ul style={{ listStyleType: "none", textAlign: "left", padding: 0, margin: 0 }}>
                    {filteredPlayers.map((player, index) => (
                        <li key={index} style={{ marginBottom: '8px' }}>
                            <button 
                                onClick={() => handlePlayerClick(player.name)}
                                style={{ 
                                    textAlign: "left", 
                                    width: "100%", 
                                    padding: "8px", 
                                    cursor: "pointer",
                                    border: "1px solid #ccc", 
                                    borderRadius: "4px",
                                    background: "#013369"
                                }}
                            >
                                {player.name}
                            </button>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default PlayerSelector;
