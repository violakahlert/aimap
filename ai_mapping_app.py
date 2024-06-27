{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "952f4f29",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-06-27 19:18:42.577 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\viola\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2024-06-27 19:18:42.591 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "# Load the data with the specified encoding\n",
    "file_path = 'AI Mapping.csv'\n",
    "try:\n",
    "    ai_mapping_df = pd.read_csv(file_path, encoding='utf-8-sig')\n",
    "except UnicodeDecodeError:\n",
    "    ai_mapping_df = pd.read_csv(file_path, encoding='ISO-8859-1')\n",
    "\n",
    "# Set the title of the Streamlit app\n",
    "st.title('AI Mapping for New Product Development')\n",
    "\n",
    "# Display the dataframe\n",
    "st.subheader('AI Tools and their Stages in the NPD Process')\n",
    "st.dataframe(ai_mapping_df)\n",
    "\n",
    "# Interactive section\n",
    "st.subheader('Explore AI Tools by NPD Stage')\n",
    "\n",
    "# Get unique stages\n",
    "stages = ai_mapping_df['Parent'].unique()\n",
    "\n",
    "# Select a stage\n",
    "selected_stage = st.selectbox('Select an NPD Stage:', stages)\n",
    "\n",
    "# Filter dataframe based on the selected stage\n",
    "filtered_df = ai_mapping_df[ai_mapping_df['Parent'] == selected_stage]\n",
    "\n",
    "# Display the filtered dataframe\n",
    "st.write(f'AI Tools for the selected stage: {selected_stage}')\n",
    "st.table(filtered_df)\n",
    "\n",
    "# Additional details (dummy content for illustration, update with real content)\n",
    "ai_details = {\n",
    "    \"1. Ideenfindung und Voruntersuchung\": \"Tools for idea generation and preliminary investigation...\",\n",
    "    \"2. Detaillierte Untersuchung (Business Case)\": \"Tools for detailed investigation and business case development...\",\n",
    "    \"3. Entwicklung\": \"Tools for development...\",\n",
    "    \"4. Tests und Validierung\": \"Tools for testing and validation...\",\n",
    "    \"5. Markteinführung\": \"Tools for market launch...\"\n",
    "}\n",
    "\n",
    "# Display details for each AI tool\n",
    "for index, row in filtered_df.iterrows():\n",
    "    tool_name = row['Child']\n",
    "    st.write(f\"**{tool_name}**: {ai_details.get(tool_name, 'Detailed information about this tool will be provided here.')}\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
