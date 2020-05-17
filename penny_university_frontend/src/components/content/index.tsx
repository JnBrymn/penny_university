import React, { useState } from 'react'
import ReactMde from 'react-mde'
import ReactMarkdown from 'react-markdown'
import * as Showdown from 'showdown'
import 'react-mde/lib/styles/css/react-mde-all.css'


type EditorTabs = 'write' | 'preview'

type ContentType = {
  content: string,
  onChange?: (content: string) => void | null,
  className?: string,
  editing?: boolean,
}

const converter = new Showdown.Converter({
  tables: true,
  simplifiedAutoLink: true,
  strikethrough: true,
  tasklists: true,
})

const Content = ({ content, onChange, editing, className }: ContentType) => {
  const [selectedTab, setSelectedTab] = useState<EditorTabs>('write')
  if (editing && onChange) {
    return (
      <ReactMde
        value={content}
        onChange={onChange}
        selectedTab={selectedTab}
        onTabChange={setSelectedTab}
        generateMarkdownPreview={(markdown: string) => Promise.resolve(converter.makeHtml(markdown))}
      />
    )
  }
  return (
    <ReactMarkdown className={className} source={content} />
  )
}

Content.defaultProps = {
  editing: false,
  className: '',
}

export default Content
