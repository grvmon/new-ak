import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PAGES_DIR = path.join(__dirname, 'src', 'content', 'pages');

async function generatePages(count) {
  console.log(`Starting to generate ${count} pages...`);
  
  // Ensure directory exists
  try {
    await fs.mkdir(PAGES_DIR, { recursive: true });
  } catch (err) {
    console.error("Failed to create directory:", err);
  }

  const batchSize = 1000;
  let created = 0;

  for (let i = 0; i < count; i += batchSize) {
    const promises = [];
    for (let j = 0; j < batchSize && (i + j) < count; j++) {
      const pageId = i + j + 1;
      const slug = `generated-page-${pageId}`;
      const filePath = path.join(PAGES_DIR, `${slug}.json`);
      
      const content = {
        title: `Institutional Asset Analysis ${pageId}`,
        content: [
          {
            type: "paragraph",
            children: [
              {
                text: `This is an automated 69-point buyer analysis report for asset #${pageId}. We filter out the noise in the market to bring you absolute clarity on infrastructure, builder history, and comparative pricing.`
              }
            ]
          },
          {
            type: "heading",
            level: 2,
            children: [{ text: "Masterplan Audit" }]
          },
          {
            type: "paragraph",
            children: [{ text: "Title deeds have been verified against the RERA database. The asset demonstrates strong yield potential based on our proprietary algorithms." }]
          }
        ]
      };

      promises.push(fs.writeFile(filePath, JSON.stringify(content, null, 2)));
    }
    
    await Promise.all(promises);
    created += promises.length;
    console.log(`Created ${created}/${count} files...`);
  }
  
  console.log('✅ Generation complete!');
}

generatePages(10000).catch(console.error);
