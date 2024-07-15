import React, { useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [text, setText] = useState('');
  const [summary, setSummary] = useState('');
  const [isLoading, setLoading] = useState(false);

  const handleSummarize = async () => {
    setLoading(true); // Set loading state to true
    try {
      const response = await axios.post('http://localhost:8000/summarize-text', { text });
      setSummary(response.data.summary);
    } catch (error) {
      console.error('Error summarizing text:', error);
      setSummary('Error summarizing text. Please try again.');
    } finally {
      setLoading(false); // Set loading state back to false
    }
  };

  return (
    <div className="container">
      <h3>Sum It Up!</h3>
      <div className="form-group">
        <label htmlFor="textInput">Enter text to summarize:</label>
        <textarea
          id="textInput"
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter your text here..."
        />
      </div>
      <div className="form-group">
        <button
          onClick={handleSummarize}
          disabled={isLoading || text.trim() === ''}
        >
          {isLoading ? 'Loading...' : 'Summarize'}
        </button>
      </div>
      <div className="summary">
        <label>Summarization result:</label>
        <textarea
          readOnly
          value={summary}
          placeholder="Summary will appear here..."
        />
      </div>
    </div>
  );
}

export default App;