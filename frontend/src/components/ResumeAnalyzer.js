import React, { useState } from 'react';

const ResumeAnalyzer = () => {
    const [file, setFile] = useState(null);
    const [results, setResults] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleFileUpload = (event) => {
        const uploadedFile = event.target.files[0];
        console.log("File details:", {
            name: uploadedFile.name,
            type: uploadedFile.type,
            size: uploadedFile.size,
            lastModified: new Date(uploadedFile.lastModified),
            extension: uploadedFile.name.split('.').pop()
        });
        setFile(uploadedFile);
    };

    const analyzeResume = async () => {
        if (!file) return;
        
        console.log("Starting analysis of file:", {
            name: file.name,
            type: file.type,
            size: file.size
        });
        
        setLoading(true);
        try {
            const formData = new FormData();
            formData.append('file', file);
        
                console.log('Attempting to send file...'); // Add this debug log

                console.log('Attempting to send file:', file);
        
                const response = await fetch('http://localhost:8001/analyze-resume', {
                    method: 'POST',
                    body: formData
                });
        
                console.log('Response:', response); // Add this debug log
                
                const result = await response.json();
                
                if (!response.ok) {
                    throw new Error(result.detail || 'Analysis failed');
                }
                
                if (result.success) {
                    setResults(result.data);
                } else {
                    throw new Error(result.error || 'Unknown error occurred');
                }
            } catch (error) {
                console.error('Detailed Error:', error); // Enhanced error logging
                alert('Failed to analyze resume. Check console for details.');
            } finally {
                setLoading(false);
            }
        };

    return (
        <div className="max-w-4xl mx-auto p-6">
            <h1 className="text-3xl font-bold mb-8 text-center">Resume Analyzer</h1>
            
            {/* File Upload Section */}
            <div className="mb-8 p-6 border rounded-lg bg-white shadow-sm">
                <input
                    type="file"
                    onChange={handleFileUpload}
                    accept=".pdf,.docx,application/pdf,application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    className="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
                />
                <button
                    onClick={analyzeResume}
                    disabled={!file || loading}
                    className="mt-4 px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:bg-gray-400"
                >
                    {loading ? 'Analyzing...' : 'Analyze Resume'}
                </button>
            </div>

            {/* Results Section */}
            {results && (
                <div className="space-y-6">
                    {/* Match Score */}
                    <div className="p-6 border rounded-lg bg-white shadow-sm">
                        <h2 className="text-xl font-semibold mb-4">Match Score</h2>
                        <div className="text-4xl font-bold text-blue-600">
                            {results.match_results.total_score}%
                        </div>
                    </div>

                    {/* Skills */}
                    <div className="p-6 border rounded-lg bg-white shadow-sm">
                        <h2 className="text-xl font-semibold mb-4">Skills Found</h2>
                        <div className="grid gap-4 md:grid-cols-3">
                            {Object.entries(results.parsed_skills).map(([category, skills]) => (
                                <div key={category}>
                                    <h3 className="font-medium mb-2 capitalize">
                                        {category.replace('_', ' ')}
                                    </h3>
                                    <ul className="list-disc list-inside text-gray-600">
                                        {skills.map((skill) => (
                                            <li key={skill}>{skill}</li>
                                        ))}
                                    </ul>
                                </div>
                            ))}
                        </div>
                    </div>

                    {/* Recommendations */}
                    <div className="p-6 border rounded-lg bg-white shadow-sm">
                        <h2 className="text-xl font-semibold mb-4">Recommendations</h2>
                        <div className="space-y-4">
                            {results.recommendations.priority_skills.map((rec, index) => (
                                <div key={index} className="p-4 bg-gray-50 rounded-md">
                                    <div className="flex items-center gap-2">
                                        <span className="font-medium">{rec.skill}</span>
                                        <span className="text-sm text-gray-500">({rec.category})</span>
                                        <span className={`ml-auto px-2 py-1 text-sm rounded ${
                                            rec.priority === 'High' ? 'bg-red-100 text-red-800' : 'bg-yellow-100 text-yellow-800'
                                        }`}>
                                            {rec.priority} Priority
                                        </span>
                                    </div>
                                    <p className="mt-2 text-gray-600">{rec.learning_path}</p>
                                </div>
                            ))}
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};

export default ResumeAnalyzer;