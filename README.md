**Install the CLI**

To work locally with your documentation, install the Command Line Interface (CLI), called mint, by running this command in your terminal:

<code>npm i -g mint</code>

You need Node.js installed on your machine. If you encounter installation issues, check the troubleshooting guide.
​

**Edit the documentation**

After setting up your environment, you can start editing your documentation files. 

For example, update the title of the introduction page:

Open your repository created during onboarding.

Open index.mdx and locate the top of the file:
index.mdx

<code>
title: "Introduction"
description: "This is the introduction to the documentation"
</code>

Update the title field to "Hello World".

index.mdx

<code>
title: "Hello World"
description: "This is the introduction to the documentation"
</code>
​

**Preview the changes**

To preview the changes locally, run the following command:

<code>mint dev</code>

Your preview will be available at localhost:3000.
​
Push the changes
When you are ready to publish your changes, push them to your repository.
