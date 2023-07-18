# 网站维护及更新
- 网址：aigcx.club 
  - 域名将于2024年6月20日左右到期，记得续期 

## 网站结构（更新会用到的）
### 内容
- site3/exampleSite/data/ 里面是网站首页文字（除最新文章外），要修改内容和图片看这里。
  - about.yml-关于我们
  - feature.yml - 关于我们2
  - service-推动各地社群营造与活动组织
  - portfolio-热点
  - funfacts-数字
  - testimonial-顾问团和秘书处
- site3/exampleSite/content/ 最新文章
  - chinese/blog
  - english/blog
- site3/exampleSite/static/images 首页及博客里的图片存储在这里
- config.toml 用于配置网站基本信息、语言、导航菜单和插件等功能的配置文件。

### 样式
- site3/layouts  
  - _default 全局的列表、文章展示
  - index.html 网站启动的首页，本网站里由多个partial（部分模板）构成。
- assets
  - assets/css/style.css 必要的样式和设计元素

### 其他（不要改）
- static - 插件
- netlify.toml 部署到netlify
- theme.toml 主题的配置文件


## 网站技术栈：
- 静态网站生成器：hugo
- 主题： [meghna-hugo/exampleSite at master · themefisher/meghna-hugo](https://github.com/themefisher/meghna-hugo/tree/master/exampleSite)
- 搭建部署：netlify
  - 在debuguself.io 组织，要更改部署等与  @liguanghe联系


## 更改内容
- 只需要在这个远程仓库中更改了文件，网站就会自动更新。
- 原理：
  - index.html 网站启动的首页，本网站里由多个partial（部分模板）构成。要增删改partial，在这个文档里，目前注释掉了一些partial，不显示。关联partial文件夹里的 *.html 等，里面是格式和排版，显示内容用代入的方法，内容储存在对应的*.yml中。
  - partial.html 从style.css 里引用字体大小等样式。
- 中英文都要同步改
### 如何更改大联盟（关于我们）

- site3/exampleSite/data/about.yml 改冒号后面的内容
- site3/exampleSite/data/service.yml 社群要求

### 如何更新白皮书、品牌规范、成员权责
- 链接放在：site3/exampleSite/data/service.yml 

### 如何添加每日寄语
- 在data/portfolio.yml 中增加：名字、图片
```
   # portfolio item loop
    - name : "Hu Yong"（更改）
      image : images/portfolio/portfolio-1.jpg
      image_webp : images/portfolio/portfolio-1.webp
      categories : ["每日寄语"]
      content : "AIGC is the new industrial revolution"
      link : "https://mp.weixin.qq.com/s/DZF09dLETODg0-HuV9Gnyw"
```

图片储存在 site3/exampleSite/static/images/portfolio 中，图片名要一致。
categories：都是每日寄语，不要改。
- 后续如果有其他专栏的话，增加：categories

### 如何更改数字
- [site3/exampleSite/static/images/portfolio at main · AIGCx/site3](https://github.com/AIGCx/site3/tree/main/exampleSite/static/images/portfolio)

### 如何增删改顾问团成员
- [site3/exampleSite/data/zh/testimonial.yml at main · AIGCx/site3](https://github.com/AIGCx/site3/blob/main/exampleSite/data/zh/testimonial.yml)
- 图片储存：[site3/exampleSite/static/images/portfolio at main · AIGCx/site3](https://github.com/AIGCx/site3/tree/main/exampleSite/static/images/portfolio)

### 如何添加新文章
- 在[site3/exampleSite/content/chinese/blog at main · AIGCx/site3](https://github.com/AIGCx/site3/tree/main/exampleSite/content/chinese/blog) 新增.md 文件
  - 如果用外链，external_link: " " 添加到引号内
  - 不用外链，将external_link: " "删掉，直接在---- 下面用markdown格式写正文。
  - 需要置顶或者靠前显示：增加：weight：1 数字越小越靠前。
- 中英文都改，英文的：[site3/exampleSite/content/english/blog at main · AIGCx/site3](https://github.com/AIGCx/site3/tree/main/exampleSite/content/english/blog)
- 图片储存在/Users/liguanghe/site3/exampleSite/static/images/blog

----
更改和搭建时[ChatGPT辅助的流水账](https://chat.openai.com/share/4480c45d-c14f-432f-a1d7-ccd3922635e7) 

---
log:
- version1 2023-07-02 @liguanghe
