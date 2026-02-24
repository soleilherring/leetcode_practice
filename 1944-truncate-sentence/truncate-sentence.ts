function truncateSentence(s: string, k: number): string {
    const result = s.split(" ").slice(0,k).join(' ')
    return result

};