![Pastel Brush Strokes Beauty Makeup Facebook Cover (1)](https://github.com/MUSKAN1903/Fashion-Dopplefinder/assets/70433658/dd6277dc-afa8-4dfa-9239-b00d00e69553)


# Fashion Dopplefinder : Discover Similar Fashion Picks
Ever looked at someone stylish and wondered if you could ever dress like that?

 - The surge of e-commerce websites in India has sparked a significant rise in online shopping across the nation.Fashion items, in particular, are the most popular and in-demand products in the thriving e-commerce market.
 - A robust, effective, and efficient recommendation system for fashion items has the potential to boost revenue, enhance customer engagement, and improve overall shopping experiences.
 - Thanks to computer vision advancements, you can now recreate the style of your favorite celebrity by simply using an image of their outfit or look.

## Fashion Industry: Statistics, Trends & Strategy

- ### The E-Commerce Fashion Revolution
> - Over the past few years, the Fashion Industry has experienced a remarkable surge in E-Commerce, transforming the way people shop for clothing, accessories, and style essentials.
> - Online platforms have become a go-to destination for fashion enthusiasts, offering a vast array of products, from trendy clothing to chic accessories, at the convenience of a few clicks.
> - As E-Commerce keeps advancing, the Fashion Industry is set for impressive growth, transforming the fashion scene in exciting and unexpected ways.

 ![image](https://github.com/MUSKAN1903/Fashion-Dopplefinder/assets/70433658/7b6316fc-64ac-429d-8395-6ede3321c48c)

- ### From Inspiration to Purchase: Unraveling Social Media's Role in Consumer Behavior
> - Nearly one-third (29%) of consumers find inspiration for their purchases through social media platforms. Influencers, brand ads, and user-generated content play a significant role in shaping their shopping decisions.
> - Social media's impact on shopping has turned it into a powerful tool for brands to connect with potential customers, creating a virtual shopping mall where captivating visuals and relatable experiences lead to more purchases.
> - This shift has transformed how people shop and engage with products, making social media a key player in modern consumer behavior.

![image](https://github.com/MUSKAN1903/Fashion-Dopplefinder/assets/70433658/1412006f-c92b-4244-8e90-768e93873e46)

- ### From Gen Z to Baby Boomers: Social Media's Impact on Fashion Choices across different age groups
> - A significant revelation in the world of online fashion shopping is that nearly half of shoppers attribute their last purchase to the influence of social media.
> - Social media's influence on fashion shopping is a powerful force that resonates across generations. Among online fashion shoppers, a staggering 55.2% of Gen Z, 50.6% of Millennials, and 27.5% of Baby Boomers reveal that their latest purchases were inspired by content found on social platforms.
> - From trendy styles showcased by influencers to engaging brand advertisements, social media's magnetic appeal drives consumers from diverse age groups to make fashion choices with just a scroll and a click.
> - These figures emphasize the significant impact of social media in driving fashion purchases across different generations, making it a crucial factor for fashion brands and marketers to consider when targeting their audience.

![image](https://github.com/MUSKAN1903/Fashion-Dopplefinder/assets/70433658/98c1edf4-c6cf-4a2a-ae17-43a75df0c3a8)


### Related Work
The Project is inspired by the research paper published by Myntra.
> [Buy Me That Look: An Approach for Recommending Fashion Products](https://arxiv.org/pdf/2008.11638.pdf)
![image](https://github.com/MUSKAN1903/Fashion-Dopplefinder/assets/70433658/6d4ff7b8-8bbb-4ffc-8218-05411af5e024)
> - The proposed method has undergone evaluation on Myntra (www.myntra.com), a prominent online fashion e-commerce platform.
> - The main objective of the method is to provide recommendations for similar fashion products based on a user query and the corresponding Product Display Page (PDP).
> - The recommendations are generated for the complete set of fashion articles worn by a model in the PDP's full-shot image, showcasing the model from head to toe.
> - What sets this method apart is its ability to suggest similar articles for all the fashion items worn by the model, going beyond just the primary article related to the user query.
> - This approach adds novelty and strength to the recommendation process, enhancing the overall shopping experience for users on the platform.

### Approach & Implementation
> - We can build two recommendation engines in this project. The first type is image based recommendation engine and second type is text based recommendation engine.
> - We have build the only image based system as of now.

### IMAGE BASED RECOMMENDATION
> - In this project, we propose a system that uses Convolutional Neural Network and the Nearest neighbor backed recommender.
> - The nearest neighbor’s algorithm is used to find the most relevant products based on the input image and recommendations are generated.
> - The nearest neighbor’s algorithm is used to find the most relevant products based on the input image and recommendations are generated.
>   
>   ![image](https://github.com/MUSKAN1903/Fashion-Dopplefinder/assets/70433658/54a645e6-65a6-4779-985b-29c3bc4c79c5)
> - We utilized transfer learning with the ResNet50 model for a new task. The data was pre-processed, and the ResNet50 model was used as a starting point.
> - Additional layers were added to fine-tune the model specifically for the current task. By keeping the ResNet50 weights frozen and updating the new layers, the model adapted its learned features effectively for the new task.
>   
> ![image](https://github.com/MUSKAN1903/Fashion-Dopplefinder/assets/70433658/e723ad03-3493-4125-b74f-bedb180267d8)

### DATASET
> - The Dataset is taken from Kaggle [Fashion Product Images Dataset](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset).
> - The dataset was too large for the system to handle,so the smaller version is used - [Fashion Product Images (Small)](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small)
> - The dataset contains 44k products with multiple category labels, descriptions and images.
> - The inventory is then run through the neural networks to classify and generate embeddings and the output is then used to generate recommendations. 
> - The Figure shows a sample set of data
> ![image](https://github.com/MUSKAN1903/Fashion-Dopplefinder/assets/70433658/bfc29745-8fa8-42aa-9e8b-82fcdb17788f)


### Recommendation Generation
> - To generate recommendations, our proposed approach uses Sklearn Nearest neighbors.
> - This allows us to find the nearest neighbors for the given input image.
> - The similarity measure used in this Project is the Euclidean distance measure.
> - The top 5 recommendations are extracted from the database and their images are displayed.

### Future Scope
> - Integrate models for object, pose, and gender detection to enhance the fashion recommendation system.
> - Implement text-based search functionality to allow users to search for specific fashion items or styles.
> - Connect the web app with an e-commerce website to enable direct shopping for recommended fashion items.





























