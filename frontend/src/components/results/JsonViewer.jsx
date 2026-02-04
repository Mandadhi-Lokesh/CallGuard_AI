import { useState } from "react";

function JsonViewer({ data }) {
    const [isExpanded, setIsExpanded] = useState(false);
    const [isCopied, setIsCopied] = useState(false);

    const handleCopy = () => {
        navigator.clipboard.writeText(JSON.stringify(data, null, 2));
        setIsCopied(true);
        setTimeout(() => setIsCopied(false), 2000);
    };

    const syntaxHighlight = (json) => {
        json = json.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
        return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function (match) {
            let cls = 'json-number';
            if (/^"/.test(match)) {
                if (/:$/.test(match)) {
                    cls = 'json-key';
                } else {
                    cls = 'json-string';
                }
            } else if (/true|false/.test(match)) {
                cls = 'json-boolean';
            } else if (/null/.test(match)) {
                cls = 'json-null';
            }
            return '<span class="' + cls + '">' + match + '</span>';
        });
    };

    const formattedJson = JSON.stringify(data, null, 2);

    return (
        <div className="json-viewer">
            <div className="json-header">
                <button
                    className="json-toggle"
                    onClick={() => setIsExpanded(!isExpanded)}
                >
                    <span className="json-icon">{isExpanded ? "▼" : "▶"}</span>
                    <span className="json-title">📄 Raw JSON Response</span>
                </button>
                {isExpanded && (
                    <button
                        className="json-copy-btn"
                        onClick={handleCopy}
                        title="Copy JSON"
                    >
                        {isCopied ? "✓ Copied!" : "📋 Copy"}
                    </button>
                )}
            </div>

            {isExpanded && (
                <div className="json-content">
                    <pre dangerouslySetInnerHTML={{ __html: syntaxHighlight(formattedJson) }} />
                </div>
            )}
        </div>
    );
}

export default JsonViewer;
