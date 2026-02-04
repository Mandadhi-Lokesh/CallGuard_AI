import { APP_CONFIG } from '../config';

export const validateAudioFile = (file) => {
    if (!file) {
        return 'No file selected.';
    }

    if (!APP_CONFIG.acceptedFormats.includes(file.type)) {
        return 'Invalid file format. Please upload MP3 or WAV.';
    }

    if (file.size > APP_CONFIG.maxAudioSize) {
        return `File too large. Maximum size is ${APP_CONFIG.maxAudioSize / (1024 * 1024)}MB.`;
    }

    return null;
};
