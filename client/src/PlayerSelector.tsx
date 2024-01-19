import React, { useState } from 'react';

type Player = {
    name: string;

    // Add other relevant properties
};

const PlayerSelector: React.FC = () => {
    const [searchTerm, setSearchTerm] = useState('');
    const [players, setPlayers] = useState<Player[]>([
        // Populate with data from Web Scraper, or call from HTML
        { name: 'Tom Brady'},
        { name: 'Eli Manning'},
        {name: 'Adit Karode'},
        {name: 'Donovan Murray'}
        // etc.
    ]);

    const filteredPlayers = players.filter(player =>
        player.name.toLowerCase().includes(searchTerm.toLowerCase())
    );

    return (
        <div>
            <input 
                type="text" 
                placeholder="Search Players" 
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
            />
            <ul>
                {filteredPlayers.map((player, index) => (
                    <li key={index}>{player.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default PlayerSelector;
