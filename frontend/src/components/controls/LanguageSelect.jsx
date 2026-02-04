import { LANGUAGES } from "../../config";

function LanguageSelect({ value, onChange }) {
    return (
        <select className="select" value={value} onChange={(e) => onChange(e.target.value)}>
            <option value="">Select Language</option>
            {LANGUAGES.map((lang) => (
                <option key={lang} value={lang}>
                    {lang}
                </option>
            ))}
        </select>
    );
}

export default LanguageSelect;
