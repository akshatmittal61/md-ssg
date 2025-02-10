Accepting input from NodeJS can be achieved using the `readline` module from native module.
Let's create a `cin` utility to take inputs with a prompt in terminal.

```typescript
import { createInterface } from "node:readline/promises";

export const cin = async (question: string = "") => {
	const readline = createInterface({
		input: process.stdin, // Use standard input stream
		output: process.stdout // Use standard output stream
	});
	
	// Ask the user a question and wait for their response
	const answer = await readline.question(question);
	
	// Close the readline interface after getting the answer
	readline.close();
	return answer;
};
```

# References

- [NodeJS Documentation](https://nodejs.dev/en/learn/accept-input-from-the-command-line-in-nodejs/)