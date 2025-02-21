// ...existing code...

async function sendVerificationCode(userId: string): Promise<void> {
    try {
        const response = await fetch(`/api/sendCode`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ userId })
        });
        if (!response.ok) {
            throw new Error(`Error sending code: ${response.statusText}`);
        }
        // Optionally, handle the successful response if needed
    } catch (error) {
        console.error('Failed to send verification code:', error);
        // Optionally, propagate or display the error
    }
}

// ...existing code...
export { sendVerificationCode };
