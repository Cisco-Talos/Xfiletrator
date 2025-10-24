import { useState, useEffect } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Input } from "@/components/ui/input";
import yaml from "js-yaml";

export default function ExfiltrationToolList() {
  const [tools, setTools] = useState([]);
  const [filtered, setFiltered] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    async function loadTools() {
      try {
        const indexRes = await fetch("/yml/index.json");
        const fileList = await indexRes.json();

        const loadedTools = await Promise.all(
          fileList.map(async (fileName) => {
            const res = await fetch(`/yml/${fileName}`);
            const text = await res.text();
            const parsed = yaml.load(text);
            parsed._filename = fileName;
            return parsed;
          })
        );

        setTools(loadedTools);
        setFiltered(loadedTools);
      } catch (error) {
        console.error("Failed to load YAML tools:", error);
      }
    }

    loadTools();
  }, []);

  useEffect(() => {
    const query = search.toLowerCase();
    const result = tools.filter(tool =>
      tool.Name?.toLowerCase().includes(query) ||
      tool.Tags?.some(tag => tag.toLowerCase().includes(query)) ||
      tool.Description?.toLowerCase().includes(query)
    );
    setFiltered(result);
  }, [search, tools]);

  return (
  <div>
    <div className="mb-6">
      <Input
        type="text"
        placeholder="Search by name, tag, or description"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        className="w-full max-w-md"
      />
    </div>

    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
      {filtered.map((tool, i) => (
        <div key={i} className="card">
          <h2>{tool.Name}</h2>
          {tool.Description && (
            <p className="text-gray-600 italic">{tool.Description}</p>
          )}
          <p><strong>Category:</strong> <span className="font-semibold">{tool.Category}</span></p>
          {tool.Capabilities?.length > 0 && (
            <div>
              <p className="font-medium mt-2">Capabilities:</p>
              <ul className="list-disc list-inside text-sm">
                {tool.Capabilities.map((cap, idx) => (
                  <li key={idx}>{cap}</li>
                ))}
              </ul>
            </div>
          )}
          {tool.Tags?.length > 0 && (
            <div className="mt-2">
              {tool.Tags.map((tag, idx) => (
                <span key={idx} className="badge">{tag}</span>
              ))}
            </div>
          )}
          {tool.UseCases?.length > 0 && (
            <div className="mt-4">
              <h3 className="font-semibold text-sm mb-2">Exfiltration Use Cases:</h3>
              <ul className="space-y-3 text-sm">
                {tool.UseCases.map((useCase, idx) => (
                  <li key={idx} className="bg-gray-100 p-2 rounded">
                    <p className="font-medium">{useCase.Title}</p>
                    <p className="italic text-gray-600">{useCase.Description}</p>
                    <pre className="bg-white p-2 mt-1 rounded border text-xs whitespace-pre-wrap">
                      {useCase.Command}
                    </pre>
                  </li>
                ))}
              </ul>
            </div>
          )}
          {tool.Detection?.length > 0 && (
            <div className="mt-4">
              <h3 className="font-semibold text-sm mb-2">Detection Opportunities:</h3>
              <ul className="space-y-2 text-sm">
                {tool.Detection.map((det, idx) => (
                  <li key={idx} className="bg-blue-50 p-2 rounded border">
                    <p><strong>Type:</strong> {det.Type}</p>
                    <p><strong>Description:</strong> {det.Description}</p>
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      ))}
    </div>
   </div>
 );
}
