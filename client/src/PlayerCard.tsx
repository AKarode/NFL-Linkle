import React from 'react';
import './PlayerCard.css'; 

type Player = {
    name: string;
    // Other player properties if needed
};

type PlayerCardProps = {
    player: Player;
};

const PlayerCard: React.FC<PlayerCardProps> = ({ player }) => {
    return (
        <div className="player-card">
            <h3>{player.name}</h3>
            {/* Add more player details here */}
        </div>
    );
};

export default PlayerCard;
